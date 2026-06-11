"""
Unit tests for Music Application - CRUD + OLAP
Tests database operations and data processing logic
"""

import pytest
import sqlite3
import pandas as pd
import os
import sys

# ── FIXTURES ──────────────────────────────────────────────────────────────

@pytest.fixture
def db():
    """Create a fresh in-memory test database with schema and seed data."""
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE user (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            user_email TEXT UNIQUE NOT NULL,
            user_mobile TEXT,
            user_address TEXT,
            joined_date TEXT
        );
        CREATE TABLE artist (
            artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_name TEXT NOT NULL,
            artist_mobile TEXT,
            artist_email TEXT,
            artist_gender TEXT,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES user(user_id)
        );
        CREATE TABLE song (
            song_id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_name TEXT NOT NULL,
            song_type TEXT,
            song_time TEXT,
            song_category TEXT,
            artist_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
        );
        CREATE TABLE ratings (
            rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_id INTEGER,
            user_id INTEGER,
            rating_value INTEGER,
            comment TEXT,
            date_rated TEXT,
            artist_id INTEGER
        );
        INSERT INTO user (user_name, user_email, user_mobile, user_address, joined_date)
            VALUES ('Alice Smith', 'alice@test.com', '07700000001', 'London', '2024-01-01'),
                   ('Bob Jones',  'bob@test.com',   '07700000002', 'Manchester', '2024-02-01'),
                   ('Carol Wu',   'carol@test.com', '07700000003', 'Birmingham', '2024-03-01');
        INSERT INTO artist (artist_name, artist_mobile, artist_email, artist_gender, user_id)
            VALUES ('The Weeknd', '07700000010', 'weeknd@music.com', 'M', 1),
                   ('Adele',      '07700000011', 'adele@music.com',  'F', 2);
        INSERT INTO song (song_name, song_type, song_time, song_category, artist_id)
            VALUES ('Blinding Lights', 'Pop',  '3:20', 'Chart',    1),
                   ('Save Your Tears',  'Pop',  '3:35', 'Chart',    1),
                   ('Hello',            'Soul', '4:55', 'Ballad',   2),
                   ('Rolling in Deep',  'Soul', '3:48', 'Ballad',   2);
        INSERT INTO ratings (song_id, user_id, rating_value, comment, date_rated, artist_id)
            VALUES (1, 1, 5, 'Amazing track', '2024-06-01', 1),
                   (1, 2, 4, 'Really good',   '2024-06-02', 1),
                   (3, 3, 5, 'Classic',       '2024-06-03', 2),
                   (4, 1, 3, 'Not bad',       '2024-06-04', 2);
    """)
    yield conn
    conn.close()


def load(conn, table, columns):
    return pd.DataFrame(conn.execute(f"SELECT * FROM {table}").fetchall(), columns=columns)


# ── CRUD TESTS ────────────────────────────────────────────────────────────

class TestRead:
    def test_load_users(self, db):
        cols = ["user_id","user_name","user_email","user_mobile","user_address","joined_date"]
        df = load(db, "user", cols)
        assert len(df) == 3

    def test_load_songs(self, db):
        cols = ["song_id","song_name","song_type","song_time","song_category","artist_id"]
        df = load(db, "song", cols)
        assert len(df) == 4

    def test_columns_present(self, db):
        cols = ["user_id","user_name","user_email","user_mobile","user_address","joined_date"]
        df = load(db, "user", cols)
        assert list(df.columns) == cols

    def test_data_types(self, db):
        cols = ["rating_id","song_id","user_id","rating_value","comment","date_rated","artist_id"]
        df = load(db, "ratings", cols)
        assert df["rating_value"].dtype in ["int64", "object"]


class TestInsert:
    def test_insert_user(self, db):
        db.execute(
            "INSERT INTO user (user_name, user_email, user_mobile, user_address, joined_date) VALUES (?,?,?,?,?)",
            ("Dave New", "dave@test.com", "07700000099", "Leeds", "2024-04-01")
        )
        db.commit()
        count = db.execute("SELECT COUNT(*) FROM user").fetchone()[0]
        assert count == 4

    def test_insert_song(self, db):
        db.execute(
            "INSERT INTO song (song_name, song_type, song_time, song_category, artist_id) VALUES (?,?,?,?,?)",
            ("New Song", "Pop", "3:00", "Chart", 1)
        )
        db.commit()
        count = db.execute("SELECT COUNT(*) FROM song").fetchone()[0]
        assert count == 5

    def test_insert_duplicate_email_fails(self, db):
        with pytest.raises(sqlite3.IntegrityError):
            db.execute(
                "INSERT INTO user (user_name, user_email) VALUES (?,?)",
                ("Duplicate", "alice@test.com")
            )


class TestDelete:
    def test_delete_user(self, db):
        db.execute("DELETE FROM user WHERE user_id = 3")
        db.commit()
        count = db.execute("SELECT COUNT(*) FROM user").fetchone()[0]
        assert count == 2

    def test_delete_nonexistent(self, db):
        db.execute("DELETE FROM user WHERE user_id = 9999")
        db.commit()
        count = db.execute("SELECT COUNT(*) FROM user").fetchone()[0]
        assert count == 3  # unchanged


class TestUpdate:
    def test_update_user_name(self, db):
        db.execute("UPDATE user SET user_name = ? WHERE user_id = 1", ("Alice Updated",))
        db.commit()
        row = db.execute("SELECT user_name FROM user WHERE user_id = 1").fetchone()
        assert row[0] == "Alice Updated"

    def test_update_rating_value(self, db):
        db.execute("UPDATE ratings SET rating_value = ? WHERE rating_id = 1", (3,))
        db.commit()
        row = db.execute("SELECT rating_value FROM ratings WHERE rating_id = 1").fetchone()
        assert row[0] == 3


# ── OLAP TESTS ────────────────────────────────────────────────────────────

class TestOLAP:

    def test_aggregate_count_by_type(self, db):
        cols = ["song_id","song_name","song_type","song_time","song_category","artist_id"]
        df = load(db, "song", cols)
        grouped = df.groupby("song_type").size().reset_index(name="count")
        assert "Pop" in grouped["song_type"].values
        assert "Soul" in grouped["song_type"].values

    def test_aggregate_avg_rating(self, db):
        cols = ["rating_id","song_id","user_id","rating_value","comment","date_rated","artist_id"]
        df = load(db, "ratings", cols)
        avg = df["rating_value"].mean()
        assert 1 <= avg <= 5

    def test_slice_by_category(self, db):
        cols = ["song_id","song_name","song_type","song_time","song_category","artist_id"]
        df = load(db, "song", cols)
        sliced = df[df["song_category"] == "Ballad"]
        assert len(sliced) == 2

    def test_roll_up_ratings_by_artist(self, db):
        cols = ["rating_id","song_id","user_id","rating_value","comment","date_rated","artist_id"]
        df = load(db, "ratings", cols)
        rolled = df.groupby("artist_id")["rating_value"].sum()
        assert rolled[1] == 9   # 5+4
        assert rolled[2] == 8   # 5+3

    def test_dice_select_columns(self, db):
        cols = ["song_id","song_name","song_type","song_time","song_category","artist_id"]
        df = load(db, "song", cols)
        diced = df[["song_name", "song_category"]]
        assert list(diced.columns) == ["song_name", "song_category"]
        assert len(diced) == 4

    def test_drill_down_notnull(self, db):
        cols = ["user_id","user_name","user_email","user_mobile","user_address","joined_date"]
        df = load(db, "user", cols)
        drilled = df[df["user_address"].notnull()]
        assert len(drilled) == 3

    def test_pivot_ratings(self, db):
        cols = ["rating_id","song_id","user_id","rating_value","comment","date_rated","artist_id"]
        df = load(db, "ratings", cols)
        pivot = df.pivot_table(index="user_id", columns="artist_id", values="rating_value", aggfunc="sum")
        assert pivot is not None
        assert pivot.shape[0] > 0


# ── DATA QUALITY TESTS ────────────────────────────────────────────────────

class TestDataQuality:

    def test_no_null_emails(self, db):
        cols = ["user_id","user_name","user_email","user_mobile","user_address","joined_date"]
        df = load(db, "user", cols)
        assert df["user_email"].isnull().sum() == 0

    def test_rating_values_in_range(self, db):
        cols = ["rating_id","song_id","user_id","rating_value","comment","date_rated","artist_id"]
        df = load(db, "ratings", cols)
        assert df["rating_value"].between(1, 5).all()

    def test_unique_user_emails(self, db):
        cols = ["user_id","user_name","user_email","user_mobile","user_address","joined_date"]
        df = load(db, "user", cols)
        assert df["user_email"].nunique() == len(df)

    def test_songs_have_artist(self, db):
        cols = ["song_id","song_name","song_type","song_time","song_category","artist_id"]
        df = load(db, "song", cols)
        assert df["artist_id"].isnull().sum() == 0

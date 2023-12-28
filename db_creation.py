import sqlite3
connection_obj=sqlite3.connect("music_db_final.db")
cursor_obj=connection_obj.cursor()

queries="""

CREATE TABLE user (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) UNIQUE NOT NULL,
    user_mobile VARCHAR(15),
    user_address TEXT,
    joined_date DATE
);

INSERT INTO user (user_name, user_email, user_mobile, user_address, joined_date)
VALUES
    (1,'Alice Johnson', 'alice@email.com', '+1-555-1234567', '123 Main St, Cityville', '2022-01-15'),
    (2,'Bob Smith', 'bob@email.com', '+1-555-9876543', '456 Elm St, Townsville', '2021-12-20'),
    (3,'Charlie Brown', 'charlie@email.com', '+1-555-5678901', '789 Oak Ave, Villageland', '2022-02-10'),
    (4,'David Wilson', 'david@email.com', '+1-555-2345678', '567 Maple Dr, Hamletown', '2021-11-05'),
    (5,'Ella Davis', 'ella@email.com', '+1-555-8765432', '890 Cedar Ln, Countryside', '2021-10-02'),
    (6,'Frank White', 'frank@email.com', '+1-555-3456789', '234 Birch Rd, Meadowville', '2022-03-25'),
    (7,'Grace Lee', 'grace@email.com', '+1-555-7654321', '456 Pine St, Hillside', '2022-01-08'),
    (8,'Harry Miller', 'harry@email.com', '+1-555-4567890', '678 Willow Ave, Riverside', '2022-04-30'),
    (10,'Ivy Turner', 'ivy@email.com', '+1-555-6543210', '123 Redwood Dr, Lakeside', '2021-12-15'),
    (11,'Jack Harris', 'jack@email.com', '+1-555-2345678', '345 Spruce Ln, Brookside', '2022-03-10'),
    (12,'Katie Clark', 'katie@email.com', '+1-555-5432109', '567 Sycamore Rd, Parkville', '2021-11-20'),
    (13,'Liam Adams', 'liam@email.com', '+1-555-8765432', '789 Oak Ave, Villageland', '2022-02-05'),
    (14,'Mia Turner', 'mia@email.com', '+1-555-3456789', '890 Cedar Ln, Countryside', '2021-10-12'),
    (15,'Noah Hall', 'noah@email.com', '+1-555-9876543', '234 Birch Rd, Meadowville', '2022-04-15'),
    (16,'Olivia Wright', 'olivia@email.com', '+1-555-1234567', '567 Maple Dr, Hamletown', '2022-01-28');

CREATE TABLE artist (
    artist_id INT PRIMARY KEY,
    artist_name VARCHAR(255) NOT NULL,
    artist_mobile VARCHAR(15),
    artist_email VARCHAR(255),
    artist_gender VARCHAR(10),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

INSERT INTO artist (artist_id, artist_name, artist_mobile, artist_email, artist_gender, user_id)
VALUES
    (1,'Adele', '+1-555-1111111', 'adele@email.com', 'Female', 1),
    (2,'Bruno Mars', '+1-555-2222222', 'bruno@email.com', 'Male', 2),
    (3,'Coldplay', '+1-555-3333333', 'coldplay@email.com', 'Mixed', 3),
    (4,'Dua Lipa', '+1-555-4444444', 'dualipa@email.com', 'Female', 4),
    (5,'Ed Sheeran', '+1-555-5555555', 'ed@email.com', 'Male', 5),
    (6,'Foo Fighters', '+1-555-6666666', 'foo@email.com', 'Mixed', 6),
    (7,'Gwen Stefani', '+1-555-7777777', 'gwen@email.com', 'Female', 7),
    (8,'Harry Styles', '+1-555-8888888', 'harry@email.com', 'Male', 8),
    (9,'Imagine Dragons', '+1-555-9999999', 'imagine@email.com', 'Mixed', 9),
    (10,'Justin Bieber', '+1-555-1010101', 'justin@email.com', 'Male', 10),
    (11,'Katy Perry', '+1-555-1212121', 'katy@email.com', 'Female', 11),
    (12,'Lady Gaga', '+1-555-1313131', 'ladygaga@email.com', 'Female', 12),
    (13,'Maroon 5', '+1-555-1414141', 'maroon5@email.com', 'Mixed', 13),
    (14,'Niall Horan', '+1-555-1515151', 'niall@email.com', 'Male', 14),
    (15,'One Direction', '+1-555-1616161', '1d@email.com', 'Mixed', 15);

CREATE TABLE song (
    song_id INT PRIMARY KEY,
    song_name VARCHAR(50),
    song_type VARCHAR(50),
    song_time TIME,
    song_category VARCHAR(50),
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);

INSERT INTO song (song_id, song_name, song_type, song_time, song_category, artist_id)
VALUES
    (1,'Song A', '3:45', 'Pop', 1),
    (2,'Song B', '4:20', 'R&B', 2),
    (3,'Song C', '3:55', 'Rock', 3),
    (4,'Song D', '3:30', 'Pop', 4),
    (5,'Song E', '4:15', 'Pop', 5),
    (6,'Song F', '3:40', 'Rock', 6),
    (7,'Song G', '3:25', 'Pop', 7),
    (8,'Song H', '4:10', 'Pop', 8),
    (9,'Song I', '3:50', 'Rock', 9),
    (10,'Song J', '3:15', 'Pop', 10),
    (11,'Song K', '3:55', 'Pop', 11),
    (12,'Song L', '3:30', 'Pop', 12),
    (13,'Song M', '4:00', 'Rock', 13),
    (14,'Song N', '4:05', 'Pop', 14),
    (15,'Song O', '3:55', 'Pop', 15);


CREATE TABLE album (
    album_id INT PRIMARY KEY,
    album_name VARCHAR(255),
    album_music_id VARCHAR(255),
    album_type VARCHAR(50),
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);
INSERT INTO album (album_id, album_name, album_music_id, album_type, artist_id)
VALUES
    (1,'25', '0123456789', 'Studio', 1),
    (2,'24K Magic', '9876543210', 'Studio', 2),
    (3,'Everyday Life', '8765432109', 'Studio', 3),
    (4,'Future Nostalgia', '7654321098', 'Studio', 4),
    (5,'÷ (Divide)', '6543210987', 'Studio', 5),
    (6,'Concrete and Gold', '5432109876', 'Studio', 6),
    (7,'Love. Angel. Music. Baby', '4321098765', 'Studio', 7),
    (8,'Fine Line', '3210987654', 'Studio', 8),
    (9,'Origins', '2109876543', 'Studio', 9),
    (10,'Changes', '1098765432', 'Studio', 10),
    (11,'Smile', '0987654321', 'Studio', 11),
    (12,'Chromatica', '987654321', 'Studio', 12),
    (13,'Red Pill Blues', '876543210', 'Studio', 13),
    (14,'Heartbreak Weather', '76543210', 'Studio', 14),
    (15,'Take Me Home', '6543210', 'Studio', 15);

CREATE TABLE chords (
    chord_id INT PRIMARY KEY,
    chord_name VARCHAR(50),
    chord VARCHAR(255),
    created_by VARCHAR(255),
    date_created DATE,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

INSERT INTO chords (chord_id,chord_name, chord, created_by, date_created, user_id)
VALUES
    (1,'C Major', 'C-E-G', 'Alice Johnson', '2022-01-18', 1),
    (2,'G Major', 'G-B-D', 'Bob Smith', '2022-01-20', 2),
    (3,'A Minor', 'A-C-E', 'Charlie Brown', '2022-01-22', 3),
    (4,'D Major', 'D-F#-A', 'David Wilson', '2022-01-24', 4),
    (5,'E Minor', 'E-G-B', 'Ella Davis', '2022-01-26', 5),
    (6,'F Major', 'F-A-C', 'Frank White', '2022-01-28', 6),
    (7,'Bb Major', 'Bb-D-F', 'Grace Lee', '2022-01-30', 7),
    (8,'G Minor', 'G-Bb-D', 'Harry Miller', '2022-02-01', 8),
    (9,'Am7', 'A-C-E-G', 'Ivy Turner', '2022-02-03', 9),
    (10,'D7', 'D-F#-A-C', 'Jack Harris', '2022-02-05', 10),
    (11,'Em7', 'E-G-B-D', 'Katie Clark', '2022-02-07', 11),
    (12,'C# Minor', 'C#-E-G#', 'Liam Adams', '2022-02-09', 12),
    (13,'F#7', 'F#-A-C#-E', 'Mia Turner', '2022-02-11', 13),
    (14,'B Major', 'B-D#-F#', 'Noah Hall', '2022-02-13', 14),
    (15,'C Minor', 'C-Eb-G', 'Olivia Wright', '2022-02-15', 15);

CREATE TABLE playlist (
    playlist_id INT PRIMARY KEY,
    playlist_name VARCHAR(255),
    playlist_song TEXT, -- Store song IDs as a comma-separated list or consider a separate linking table
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

INSERT INTO playlist (playlist_id,playlist_name, playlist_song, user_id)
VALUES
    
    (2,'Chill Vibes', '2,4,6,8,10,12', 2),
    (3,'Rock Classics', '3,6,9,12,15', 3),
    (4,'Pop Hits', '1,4,7,10,13', 4),
    (5,'Indie Gems', '2,5,8,11,14', 5),
    (6,'Party Anthems', '3,6,9,12,15', 6),
    (7,'Road Trip Tunes', '1,4,7,10,13', 7),
    (8,'Jazz Fusion', '2,5,8,11,14', 8),
    (9,'Acoustic Bliss', '1,4,7,10,13', 9),
    (10,'R&B Grooves', '2,5,8,11,14', 10),
    (11,'Dance Party', '3,6,9,12,15', 11),
    (12,'Country Hits', '1,4,7,10,13', 12),
    (13,'Classical Gems', '2,5,8,11,14', 13),
    (14,'Hip-Hop Vibes', '3,6,9,12,15', 14),
    (15,'Reggae Roots', '1,4,7,10,13', 15);

CREATE TABLE gener (
    gener_id INT PRIMARY KEY,
    gener_name VARCHAR(50),
    description TEXT,
    created_date DATE
);

INSERT INTO gener (gener_id, gener_name, description, created_date)
VALUES
    (1,'Pop', 'Popular music', '2022-01-15'),
    (2,'Rock', 'Rock and roll', '2022-01-16'),
    (3,'R&B', 'Rhythm and blues', '2022-01-17'),
    (4,'Jazz', 'Jazz and blues', '2022-01-18'),
    (5,'Hip-Hop', 'Hip-hop and rap', '2022-01-19'),
    (6,'Country', 'Country and western', '2022-01-20'),
    (7,'Classical', 'Classical music', '2022-01-21'),
    (8,'Reggae', 'Reggae and ska', '2022-01-22'),
    (9,'Blues', 'Blues and soul', '2022-01-23'),
    (10,'Electronic', 'Electronic music', '2022-01-24'),
    (11,'Folk', 'Folk and acoustic', '2022-01-25'),
    (12,'Indie', 'Indie and alternative', '2022-01-26'),
    (13,'Metal', 'Heavy metal', '2022-01-27'),
    (14,'Punk', 'Punk rock', '2022-01-28'),
    (15, 'World', 'World music', '2022-01-29');

CREATE TABLE lyric (
    lyric_id INT PRIMARY KEY,
    song_id INT,
    language VARCHAR(50),
    date_created DATE,
    FOREIGN KEY (song_id) REFERENCES song(song_id)
);

INSERT INTO lyric (lyric_id, song_id, language, date_created)
VALUES
    (1,1, 'English', '2022-01-18'),
    (2,2, 'English', '2022-01-20'),
    (3,3, 'English', '2022-01-22'),
    (4,4, 'English', '2022-01-24'),
    (5,5, 'English', '2022-01-26'),
    (6,6, 'English', '2022-01-28'),
    (7,7, 'English', '2022-01-30'),
    (8,8, 'English', '2022-02-01'),
    (9,9, 'English', '2022-02-03'),
    (10,10, 'English', '2022-02-05'),
    (11,11, 'English', '2022-02-07'),
    (12,12, 'English', '2022-02-09'),
    (13,13, 'English', '2022-02-11'),
    (14,14, 'English', '2022-02-13'),
    (15,15, 'English', '2022-02-15');

CREATE TABLE instrument (
    instrument_id INT PRIMARY KEY,
    instrument_name VARCHAR(255) NOT NULL,
    instrument_type VARCHAR(50),
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);

INSERT INTO instrument (instrument_id, instrument_name, instrument_type, artist_id)
VALUES
    (1, 'Guitar', 'String', 1),
    (2, 'Piano', 'Keyboard', 2),
    (3, 'Drums', 'Percussion', 3),
    (4, 'Bass Guitar', 'String', 4),
    (5, 'Violin', 'String', 5),
    (6, 'Trumpet', 'Brass', 6),
    (7, 'Saxophone', 'Woodwind', 7),
    (8, 'Flute', 'Woodwind', 8),
    (9, 'Bassoon', 'Woodwind', 9),
    (10, 'Harmonica', 'Wind', 10),
    (11, 'Synthesizer', 'Electronic', 11),
    (12, 'Accordion', 'Keyboard', 12),
    (13, 'Banjo', 'String', 13),
    (14, 'Xylophone', 'Percussion', 14),
    (15, 'Bagpipes', 'Wind', 15);
CREATE TABLE ratings (
    rating_id INT PRIMARY KEY,
    song_id INT,
    user_id INT,
    rating_value INT,
    comment TEXT,
    date_rated DATE,
    artist_id int,
    FOREIGN KEY (song_id) REFERENCES song(song_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);

INSERT INTO ratings (rating_id, song_id, user_id, rating_value, comment, date_rated, artist_id)
VALUES
    (1, 1, 1, 5, 'Great song!', '2022-01-18',1),
    (2, 2, 2, 4, 'Nice melody.', '2022-01-20',2),
    (3, 3, 3, 5, 'Rocking performance!', '2022-01-22',3),
    (4, 4, 4, 4, 'Catchy tune.', '2022-01-24',4),
    (5, 5, 5, 3, 'Decent song.', '2022-01-26',5),
    (6, 6, 6, 5, 'Awesome drumming.', '2022-01-28',6),
    (7, 7, 7, 4, 'Smooth sax.', '2022-01-30',7),
    (8, 8, 8, 4, 'Beautiful piano.', '2022-02-01',8),
    (9, 9, 9, 3, 'Interesting instrument.', '2022-02-03',9),
    (10, 10, 10, 5, 'Harmonica magic!', '2022-02-05',10),
    (11, 11, 1, 4, 'Cool synth sound.', '2022-02-07',11),
    (12, 12, 2, 3, 'Accordion vibes.', '2022-02-09',12),
    (13, 13, 3, 5, 'Banjo twang.', '2022-02-11',13),
    (14, 14, 4, 4, 'Xylophone melodies.', '2022-02-13',14),
    (15, 15, 5, 3, 'Bagpipes mood.', '2022-02-15', 15);

CREATE VIEW artist_instruments AS
SELECT
    a.artist_name,
    a.artist_email,
    i.instrument_name
FROM
    artist a
LEFT JOIN
    instrument i ON a.artist_id = i.artist_id;
    
    CREATE VIEW top_rated_songs AS
SELECT
    s.song_name,
    AVG(r.rating_value) AS average_rating
FROM
    song s
LEFT JOIN
    rating r ON s.song_id = r.song_id
GROUP BY
    s.song_name
HAVING
    AVG(r.rating_value) >= 4;
INSERT INTO song (song_id,song_name)
VALUES
    (1,'Eternal Love'),
    (2,'Summer Breeze'),
    (3,'Rock Revolution'),
    (4,'City Lights'),
    (5,'Ocean Waves'),
    (6,'Jazzed Up'),
    (7,'Melancholy Blues'),
    (8,'Dreamy Night'),
    (9,'Electric Dreams'),
    (10,'Harmonious Melodies'),
    (11,'Mystic Echoes'),
    (12,'Acoustic Serenade'),
    (13,'Soulful Rhythms'),
    (14,'Funky Grooves'),
    (15,'Classical Elegance');


CREATE TABLE songs (
    song_id INT PRIMARY KEY,
    Song_name VARCHAR(50),
    song_type VARCHAR(50),
    song_time TIME,
    song_category VARCHAR(50),
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);

CREATE TEMPORARY TABLE temp_table (
    temp_id INT PRIMARY KEY,
    temp_data VARCHAR(255)
);

DELIMITER $$
CREATE TRIGGER log_song_changes
AFTER INSERT ON song
FOR EACH ROW
BEGIN
    INSERT INTO song_change_log (song_id, change_type, change_date)
    VALUES (NEW.song_id, 'INSERT', NOW());
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE get_songs_by_artist(IN artist_id INT)
BEGIN
    SELECT * FROM song WHERE artist_id = artist_id;
END $$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION calculate_average_rating(song_id INT)
RETURNS DECIMAL(3,2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE avg_rating DECIMAL(3,2);
    SELECT AVG(rating_value) INTO avg_rating FROM rating WHERE song_id = song_id;
    RETURN avg_rating;
END $$
DELIMITER ;

CREATE VIEW song_ratings AS
SELECT
    s.song_name,
    AVG(r.rating_value) AS average_rating,
    COUNT(r.rating_id) AS number_of_ratings
FROM
    song s
LEFT JOIN
    rating r ON s.song_id = r.song_id
GROUP BY
    s.song_name;

CREATE INDEX idx_artist_name ON artist (artist_name);
show index from location;


CREATE VIEW top_artists_by_songs AS
SELECT
    a.artist_name,
    COUNT(s.song_id) AS number_of_songs
FROM
    artist a
LEFT JOIN
    song s ON a.artist_id = s.artist_id
GROUP BY
    a.artist_name
ORDER BY
    number_of_songs DESC;

CREATE VIEW songs_by_genre AS
SELECT
    gener_name,
    song_name
FROM
    gener
LEFT JOIN
    song  ON gener_id = gener_id;

-- Create a temporary table to store user data
CREATE TEMPORARY TABLE temp_user_data0 AS select * from user;
Select * from User ;

DELIMITER $$

DELIMITER $$
CREATE TRIGGER update_rating_statistics
AFTER INSERT ON rating
FOR EACH ROW
BEGIN
UPDATE song
SET song_rating = (SELECT AVG(rating_value) FROM rating WHERE song_id = NEW.song_id)
WHERE song_id = NEW.song_id;
END $$
DELIMITER ;


DELIMITER $$

CREATE TRIGGER enforce_album_type_consistency
BEFORE INSERT ON album
FOR EACH ROW
BEGIN
    DECLARE artist_gender VARCHAR(10);
    SELECT artist_gender INTO artist_gender FROM artist WHERE artist_id = NEW.artist_id;

    IF NEW.album_type != artist_gender THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Album type does not match artist gender.';
    END IF;
END $$

DELIMITER ;

DELIMITER $$

DELIMITER $$
CREATE PROCEDURE add_new_song(
IN song_name VARCHAR(255),
IN song_type VARCHAR(50),
IN song_time INT,
IN song_category VARCHAR(50),
IN artist_id INT
)
BEGIN
INSERT INTO song (song_name, song_type, song_time, song_category, artist_id)
VALUES (song_name, song_type, song_time, song_category, artist_id);
END $$
DELIMITER ;

DELIMITER $$

CREATE PROCEDURE delete_playlist(IN playlist_id INT)
BEGIN
    DELETE FROM playlist WHERE playlist_id = playlist_id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE calculate_song_duration(IN song_id INT)
BEGIN
    DECLARE song_duration VARCHAR(20);
    SELECT CONCAT(FLOOR(song_time / 60), 'm ', song_time % 60, 's') INTO song_duration FROM song WHERE song_id = song_id;
    SELECT song_duration;
END $$

DELIMITER ;
DELIMITER $$

CREATE FUNCTION count_songs_by_artist(artist_id INT)
RETURNS INT
READS SQL DATA
BEGIN
    DECLARE song_count INT;
    SELECT COUNT(*) INTO song_count FROM song WHERE artist_id = artist_id;
    RETURN song_count;
END $$

DELIMITER ;
SET GLOBAL log_bin_trust_function_creators = 1;

DELIMITER $$

CREATE FUNCTION has_lyrics(song_id INT)
RETURNS BOOLEAN
BEGIN
    DECLARE has_lyrics_flag BOOLEAN;
    SELECT COUNT(*) INTO has_lyrics_flag FROM lyric WHERE song_id = song_id;
    RETURN IF(has_lyrics_flag > 0, TRUE, FALSE);
END $$

DELIMITER ;
SET SQL_SAFE_UPDATES = 0;

DELIMITER $$

CREATE PROCEDURE calculate_song_duration1(IN song_id INT)
BEGIN
    DECLARE song_duration VARCHAR(20);
    SELECT CONCAT(FLOOR(song_time / 60), 'm ', song_time % 60, 's') INTO song_duration FROM song WHERE song_id = song_id LIMIT 1;
    SELECT song_duration AS 'Song Duration';
END $$

DELIMITER ;

# Drill Down Functionality
elif app_mode == "Drill Down":
    st.subheader("Drill Down Functionality")

    # Select drill down column
    drill_down_col = st.selectbox("Select column to drill down:", table_columns[table])

    if drill_down_col:
        # Filter data based on drill down column
        filtered_data = data[data[drill_down_col].notnull()]

        # Display drilled down data
        st.subheader("Drilled Down Data")
        st.table(filtered_data)

        # Save drilled down data to the database
        filtered_data.to_sql('drilled_data', conn, if_exists='replace', index=False)
END $$

DELIMITER ;
# Roll Up Functionality
elif app_mode == "Roll Up":
    st.subheader("Roll Up Functionality")

    # Select roll up column
    roll_up_col = st.selectbox("Select column to roll up:", table_columns[table])

    if roll_up_col:
        # Group data based on roll up column
        rolled_up_data = data.groupby(roll_up_col).sum()

        # Display rolled up data
        st.subheader("Rolled Up Data")
        st.table(rolled_up_data)

        # Save rolled up data to the database
        rolled_up_data.to_sql('rolled_up_data', conn, if_exists='replace', index=False)
END $$

DELIMITER ;

# Dice Functionality
elif app_mode == "Dice":
    st.subheader("Dice Functionality")

    # Select dice columns and values
    dice_cols = []
    for col in table_columns[table]:
        if st.checkbox(col):
            dice_cols.append(col)

    if dice_cols:
        # Filter data based on dice columns
        diced_data = data[dice_cols]

        # Display diced data
        st.subheader("Diced Data")
        st.table(diced_data)

        # Save diced data to the database
        diced_data.to_sql('diced_data', conn, if_exists='replace', index=False)
END $$

DELIMITER ;
# Slice Functionality
elif app_mode == "Slice":
    st.subheader("Slice Functionality")

    # Select slice column and value
    slice_col = st.selectbox("Select column to slice:", table_columns[table])
    slice_value = st.text_input("Enter value to slice:")

    if slice_col and slice_value:
        # Filter data based on slice column and value
        sliced_data = data[data[slice_col] == slice_value]

        # Display sliced data
        st.subheader("Sliced Data")
        st.table(sliced_data)

        # Save sliced data to the database
        sliced_data.to_sql('sliced_data', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
"""


cursor_obj.executescript(queries)


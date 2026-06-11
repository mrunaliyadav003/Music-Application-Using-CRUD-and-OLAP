import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import sqlite3

# ── PAGE CONFIG ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Music App",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

page_bg_img = '''
<style>
.stApp {
    background-size: cover;
    background-image: url('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJoDsppA6x2JI7WQnTgfnYaoTFVW4W48Sg-VDTMjM_l5knjx7o0_pURlt0SDAfHU0mk_jZQPCZojgLiNFQYq9ak_2I2WsNwjrQ_c8OBc-w8f4ATsuq0nK3FmY8NfHZrhwPPatB9qM2Ugl4UjFQI4goBPqTTjJECavIYOgNCLDVlWkB4CBvcBeeCoHabQ/s2560/wallpaper-for-setup-gamer-2560x1440.jpg')
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
components.html("""<h1><p style='color:white; margin-bottom:-40px; font-family:Arial'><u>Music App - CRUD & OLAP Operations</u></p></h1>""")

# ── CONSTANTS ────────────────────────────────────────────────────────────
tables = ["user", "artist", "song", "album", "chords", "playlist", "gener", "lyric", "instrument", "ratings"]

table_columns = {
    "user":       ["user_id", "user_name", "user_email", "user_mobile", "user_address", "joined_date"],
    "artist":     ["artist_id", "artist_name", "artist_mobile", "artist_email", "artist_gender", "user_id"],
    "song":       ["song_id", "song_name", "song_type", "song_time", "song_category", "artist_id"],
    "album":      ["album_id", "album_name", "album_music_id", "album_type", "artist_id"],
    "chords":     ["chord_id", "chord_name", "chord", "created_by", "date_created", "user_id"],
    "playlist":   ["playlist_id", "playlist_name", "playlist_song", "user_id"],
    "gener":      ["gener_id", "gener_name", "description", "created_date"],
    "lyric":      ["lyric_id", "song_id", "language", "date_created"],
    "instrument": ["instrument_id", "instrument_name", "instrument_type", "artist_id"],
    "ratings":    ["rating_id", "song_id", "user_id", "rating_value", "comment", "date_rated", "artist_id"],
}

# ── DB CONNECTION ─────────────────────────────────────────────────────────
@st.cache_resource
def get_connection():
    return sqlite3.connect("music_db_final.db", check_same_thread=False)

conn = get_connection()

def load_table(table):
    query = f"SELECT * FROM {table}"
    return pd.DataFrame(conn.execute(query).fetchall(), columns=table_columns[table])

def commit_insert(table, row_dict):
    cols = ", ".join(row_dict.keys())
    vals = ", ".join(["?" for _ in row_dict])
    conn.execute(f"INSERT INTO {table} ({cols}) VALUES ({vals})", list(row_dict.values()))
    conn.commit()

def commit_delete(table, id_col, id_val):
    conn.execute(f"DELETE FROM {table} WHERE {id_col} = ?", (id_val,))
    conn.commit()

def commit_update(table, id_col, id_val, col, val):
    conn.execute(f"UPDATE {table} SET {col} = ? WHERE {id_col} = ?", (val, id_val))
    conn.commit()

# ── SIDEBAR ───────────────────────────────────────────────────────────────
app_mode = st.sidebar.selectbox(
    "Select Operation",
    ["View & Statistics", "Insert", "Delete", "Update",
     "OLAP - Aggregate", "OLAP - Pivot", "OLAP - Slice", "OLAP - Dice", "OLAP - Roll Up", "OLAP - Drill Down"]
)

table = st.selectbox("Select Table", tables)
data = load_table(table)
id_col = table_columns[table][0]

st.subheader(f"Table: {table}  ({len(data)} records)")
st.dataframe(data, use_container_width=True)

# ── VIEW & STATISTICS ─────────────────────────────────────────────────────
if app_mode == "View & Statistics":
    st.subheader("Statistics")
    st.dataframe(data.describe().T, use_container_width=True)

    st.subheader("Unique Value Count per Column")
    col = st.selectbox("Select column", table_columns[table])
    if col:
        st.write(f"Total unique values in **{col}**: {data[col].nunique()}")
        try:
            st.bar_chart(data[col].value_counts())
        except Exception:
            st.info("Chart not available for this column type.")

# ── INSERT ────────────────────────────────────────────────────────────────
elif app_mode == "Insert":
    st.subheader(f"Insert into {table}")
    cols_to_fill = table_columns[table][1:]  # skip auto-id
    inputs = {}
    for c in cols_to_fill:
        inputs[c] = st.text_input(f"{c}")

    if st.button("Insert Record"):
        if all(v.strip() for v in inputs.values()):
            try:
                # Cast numeric-looking values
                typed = {}
                for k, v in inputs.items():
                    try:
                        typed[k] = int(v)
                    except ValueError:
                        try:
                            typed[k] = float(v)
                        except ValueError:
                            typed[k] = v
                commit_insert(table, typed)
                st.success("Record inserted successfully!")
                st.dataframe(load_table(table), use_container_width=True)
            except Exception as e:
                st.error(f"Insert failed: {e}")
        else:
            st.warning("Please fill in all fields.")

# ── DELETE ────────────────────────────────────────────────────────────────
elif app_mode == "Delete":
    st.subheader(f"Delete from {table}")
    id_val = st.text_input(f"Enter {id_col} to delete")
    if st.button("Delete Record"):
        if id_val.strip():
            try:
                commit_delete(table, id_col, int(id_val))
                st.success(f"Record with {id_col} = {id_val} deleted.")
                st.dataframe(load_table(table), use_container_width=True)
            except Exception as e:
                st.error(f"Delete failed: {e}")
        else:
            st.warning(f"Please enter a {id_col}.")

# ── UPDATE ────────────────────────────────────────────────────────────────
elif app_mode == "Update":
    st.subheader(f"Update {table}")
    id_val = st.text_input(f"Enter {id_col} to update")
    col_to_update = st.selectbox("Column to update", table_columns[table][1:])
    new_val = st.text_input("New value")
    if st.button("Update Record"):
        if id_val.strip() and new_val.strip():
            try:
                typed_val = new_val
                try:
                    typed_val = int(new_val)
                except ValueError:
                    try:
                        typed_val = float(new_val)
                    except ValueError:
                        pass
                commit_update(table, id_col, int(id_val), col_to_update, typed_val)
                st.success("Record updated successfully!")
                st.dataframe(load_table(table), use_container_width=True)
            except Exception as e:
                st.error(f"Update failed: {e}")
        else:
            st.warning("Please fill in all fields.")

# ── OLAP: AGGREGATE ───────────────────────────────────────────────────────
elif app_mode == "OLAP - Aggregate":
    st.subheader("Aggregate Functions (OLAP)")
    cols = st.multiselect("Group by columns", table_columns[table])
    agg_functions = st.multiselect("Aggregate functions", ["count", "mean", "sum", "min", "max"])
    numeric_cols = data.select_dtypes(include="number").columns.tolist()
    selected_cols = st.multiselect("Aggregate on columns", numeric_cols)
    if cols and agg_functions and selected_cols:
        try:
            result = data.groupby(cols)[selected_cols].agg(agg_functions)
            st.dataframe(result, use_container_width=True)
        except Exception as e:
            st.error(f"Aggregation error: {e}")

# ── OLAP: PIVOT ───────────────────────────────────────────────────────────
elif app_mode == "OLAP - Pivot":
    st.subheader("Pivot Table")
    index_col = st.selectbox("Index column", table_columns[table])
    pivot_col = st.selectbox("Pivot column", table_columns[table])
    numeric_cols = data.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        value_col = st.selectbox("Value column (numeric)", numeric_cols)
        if st.button("Generate Pivot"):
            try:
                pivot = data.pivot_table(index=index_col, columns=pivot_col, values=value_col, aggfunc="sum")
                st.dataframe(pivot, use_container_width=True)
            except Exception as e:
                st.error(f"Pivot error: {e}")
    else:
        st.info("No numeric columns in this table for pivot aggregation.")

# ── OLAP: SLICE ───────────────────────────────────────────────────────────
elif app_mode == "OLAP - Slice":
    st.subheader("Slice - Filter by column value")
    slice_col = st.selectbox("Column to slice on", table_columns[table])
    unique_vals = data[slice_col].dropna().unique().tolist()
    slice_val = st.selectbox("Select value", unique_vals)
    if slice_val is not None:
        sliced = data[data[slice_col] == slice_val]
        st.write(f"{len(sliced)} records where {slice_col} = {slice_val}")
        st.dataframe(sliced, use_container_width=True)

# ── OLAP: DICE ────────────────────────────────────────────────────────────
elif app_mode == "OLAP - Dice":
    st.subheader("Dice - Select subset of columns")
    dice_cols = st.multiselect("Select columns to include", table_columns[table], default=table_columns[table])
    if dice_cols:
        st.dataframe(data[dice_cols], use_container_width=True)

# ── OLAP: ROLL UP ─────────────────────────────────────────────────────────
elif app_mode == "OLAP - Roll Up":
    st.subheader("Roll Up - Group and summarise")
    roll_col = st.selectbox("Group by column", table_columns[table])
    numeric_cols = data.select_dtypes(include="number").columns.tolist()
    if numeric_cols and roll_col:
        try:
            rolled = data.groupby(roll_col)[numeric_cols].sum()
            st.dataframe(rolled, use_container_width=True)
        except Exception as e:
            st.error(f"Roll up error: {e}")
    else:
        st.info("No numeric columns available for roll up.")

# ── OLAP: DRILL DOWN ─────────────────────────────────────────────────────
elif app_mode == "OLAP - Drill Down":
    st.subheader("Drill Down - Filter by non-null values")
    drill_col = st.selectbox("Column to drill into", table_columns[table])
    if drill_col:
        filtered = data[data[drill_col].notnull()]
        val_filter = st.text_input(f"Optional: filter {drill_col} contains")
        if val_filter:
            filtered = filtered[filtered[drill_col].astype(str).str.contains(val_filter, case=False, na=False)]
        st.write(f"{len(filtered)} records")
        st.dataframe(filtered, use_container_width=True)

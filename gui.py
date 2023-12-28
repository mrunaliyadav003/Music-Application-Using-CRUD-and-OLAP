import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

import sqlite3


#streamlit section
st.set_page_config(
    page_title="Music GUI",
    page_icon="https://thumbs.dreamstime.com/z/music-icon-audio-sound-media-musical-design-elements-staff-note-symbol-your-web-site-logo-app-ui-vecto-vector-125354786.jpg",
    layout="centered",
    initial_sidebar_state="expanded")

page_bg_img='''
    <style>
    .stApp{
    background-size:cover;
    background-image:url('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJoDsppA6x2JI7WQnTgfnYaoTFVW4W48Sg-VDTMjM_l5knjx7o0_pURlt0SDAfHU0mk_jZQPCZojgLiNFQYq9ak_2I2WsNwjrQ_c8OBc-w8f4ATsuq0nK3FmY8NfHZrhwPPatB9qM2Ugl4UjFQI4goBPqTTjJECavIYOgNCLDVlWkB4CBvcBeeCoHabQ/s2560/wallpaper-for-setup-gamer-2560x1440.jpg')
    }
    </style>
    '''
st.markdown(page_bg_img, unsafe_allow_html=True)

components.html("""<h1><p class='font-family:Arial' style='color:white; margin-bottom:-40px'><u>Music app CRUD Operations</u></p></h1>""")

app_mode=st.sidebar.selectbox('Select Page',['Aggregate functions','Insert','Delete','Update'])

tables = ["user", "artist", "song", "album", "chords", "playlist", "gener", "lyric", "instrument", "ratings"]

cloumns_table=dict()

table_columns = {
    "user": ["user_id", "user_name", "user_email", "user_mobile", "user_address", "joined_date"],
    "artist": ["artist_id", "artist_name", "artist_mobile", "artist_email", "artist_gender", "user_id"],
    "song": ["song_id", "song_name", "song_type", "song_time", "song_category", "artist_id"],
    "album": ["album_id", "album_name", "album_music_id", "album_type", "artist_id"],
    "chords": ["chord_id", "chord_name", "chord", "created_by", "date_created", "user_id"],
    "playlist": ["playlist_id", "playlist_name", "playlist_song", "user_id"],
    "gener": ["gener_id", "gener_name", "description", "created_date"],
    "lyric": ["lyric_id", "song_id", "language", "date_created"],
    "instrument": ["instrument_id", "instrument_name", "instrument_type", "artist_id"],
    "ratings": ["rating_id", "song_id", "user_id", "rating_value", "comment", "date_rated", "artist_id"],
}


def update(df, id_to_update_at, column_name, column_value):
    df.at[id_to_update_at, column_name] = column_value
    # List of table names
    table_names = ["user", "artist", "song", "album", "chords", "playlist", "gener", "lyric", "instrument", "ratings"]

    # Loop through each table
    for table_name in table_names:
        df = globals()[f"df_{table_name}"]  # Get the DataFrame dynamically
        df.set_index(f"{table_name}_id", inplace=True)
        
        if text == table_name:
            id_value = input(f"Enter {table_name} ID: ")
            column_to_update = input("Enter column to update: ")
            update_value = input("Enter update value: ")
            update(df, id_value, column_to_update, update_value)

connection_obj=sqlite3.connect("music_db_final.db")
cursor_obj=connection_obj.cursor()
table=st.selectbox("Select the table",tables)
query="select * from " + table
data=pd.DataFrame(cursor_obj.execute(query).fetchall(),columns=table_columns[table])

st.subheader("Table")
st.table(data)

if app_mode=="Aggregate functions":  
    st.subheader("Statistics about the table")
    st.table(data.describe().T)
    st.subheader("Get the count of unique attribute")
    col=st.selectbox("Select the column",table_columns[table])
    if col:
        text="Total no. of unique columns is "+ str(data[col].nunique())
        st.write(text)
        st.bar_chart(data[col])
elif app_mode=="Delete":
    st.subheader("Delete the records")
    a="Enter {0} ID to delete".format(table)
    name=table+"_id"
    delete_artist_id = st.text_input(a)
    df=data
    if table and delete_artist_id:
        data=df.drop(df[df[name]==int(delete_artist_id)].index)
        st.subheader("Updated table")
        st.table(data)
elif app_mode=="Insert":
    st.subheader("Insert the data")
    if table == "user":
        name = st.text_input("Enter user name: ")
        email = st.text_input("Enter user email: ")
        mobile = st.text_input("Enter user mobile: ")
        address = st.text_input("Enter user address: ")
        joined_date = st.text_input("Enter joined date: ")
        
        if joined_date:
            user_data = {
                "user_name": name,
                "user_email": email,
                "user_mobile": mobile,
                "user_address": address,
                "joined_date": joined_date,
            }
        
            data=data.append(user_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(data)
    # Artist
    if table == "artist":
        artist_id = st.text_input("Enter artist ID: ")
        artist_name = st.text_input("Enter artist name: ")
        artist_mobile = st.text_input("Enter artist mobile: ")
        artist_email = st.text_input("Enter artist email: ")
        artist_gender = st.text_input("Enter artist gender: ")
        user_id = st.text_input("Enter user ID: ")
        
        if user_id:     
            artist_data = {
                "artist_id": int(artist_id),
                "artist_name": artist_name,
                "artist_mobile": artist_mobile,
                "artist_email": artist_email,
                "artist_gender": artist_gender,
                "user_id": user_id,
            }
            data=data.append(artist_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(data)
       
    # Song
    if table == "song":
        song_id = st.text_input("Enter song ID: ")
        song_name = st.text_input("Enter song name: ")
        song_type = st.text_input("Enter song type: ")
        song_time = st.text_input("Enter song time: ")
        song_category = st.text_input("Enter song category: ")
        artist_id = st.text_input("Enter artist ID: ")
        
        if artist_id:
            song_data = {
                "song_id": int(song_id),
                "song_name": song_name,
                "song_type": song_type,
                "song_time": song_time,
                "song_category": song_category,
                "artist_id": int(artist_id),
            }

            data=data.append(song_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(data)

    # Album
    if table == "album":
        album_id = st.text_input("Enter album ID: ")
        album_name = st.text_input("Enter album name: ")
        album_music_id = st.text_input("Enter album music ID: ")
        album_type = st.text_input("Enter album type: ")
        artist_id = st.text_input("Enter artist ID: ")
        
        if artist_id:
            album_data = {
                "album_id": int(album_id),
                "album_name": album_name,
                "album_music_id": album_music_id,
                "album_type": album_type,
                "artist_id": int(artist_id),
            }

            data=data.append(album_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(data)

    # Chords
    if table == "chords":
        chord_id = st.text_input("Enter chord ID: ")
        chord_name = st.text_input("Enter chord name: ")
        chord = st.text_input("Enter chord: ")
        created_by = st.text_input("Enter created by: ")
        date_created = st.text_input("Enter date created: ")
        user_id = st.text_input("Enter user ID: ")
        
        if user_id:
            chords_data = {
                "chord_id": int(chord_id),
                "chord_name": chord_name,
                "chord": chord,
                "created_by": created_by,
                "date_created": date_created,
                "user_id": int(user_id),
            }

            data=data.append(chords_data_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(data)

    # Playlist
    if table == "playlist":
        playlist_id = st.text_input("Enter playlist ID: ")
        playlist_name = st.text_input("Enter playlist name: ")
        playlist_song = st.text_input("Enter playlist song: ")
        user_id = st.text_input("Enter user ID: ")
        
        if user_id:
            playlist_data = {
                "playlist_id": int(playlist_id),
                "playlist_name": playlist_name,
                "playlist_song": playlist_song,
                "user_id": int(user_id),
            }

            data=data.append(playlist_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(data)
    # Gener
    if table == "gener":
        gener_id = st.text_input("Enter gener ID: ")
        gener_name = st.text_input("Enter gener name: ")
        description = st.text_input("Enter description: ")
        created_date = st.text_input("Enter created date: ")
        
        if created_date:
            gener_data = {
                "gener_id": int(gener_id),
                "gener_name": gener_name,
                "description": description,
                "created_date": created_date,
            }

            data=data.append(gener_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(data)

    # Lyric
    if table == "lyric":
        lyric_id = st.text_input("Enter lyric ID: ")
        song_id = st.text_input("Enter song ID: ")
        language = st.text_input("Enter language: ")
        date_created = st.text_input("Enter date created: ")
        
        if date_created:
            lyric_data = {
                "lyric_id": int(lyric_id),
                "song_id": int(song_id),
                "language": language,
                "date_created": date_created,
            }

            data=data.append(lyric_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(data)

    # Instrument
    if table == "instrument":
        instrument_id = st.text_input("Enter instrument ID: ")
        instrument_name = st.text_input("Enter instrument name: ")
        instrument_type = st.text_input("Enter instrument type: ")
        artist_id = st.text_input("Enter artist ID: ")
        
        if artist_id:
            instrument_data = {
                "instrument_id": int(instrument_id),
                "instrument_name": instrument_name,
                "instrument_type": instrument_type,
                "artist_id": int(artist_id),
            }

            data=data.append(artist_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(instrument_data)

    # Ratings
    if table == "ratings":
        rating_id = st.text_input("Enter rating ID: ")
        song_id = st.text_input("Enter song ID: ")
        user_id = st.text_input("Enter user ID: ")
        rating_value = st.text_input("Enter rating value: ")
        comment = st.text_input("Enter comment: ")
        date_rated = st.text_input("Enter date rated: ")
        artist_id = st.text_input("Enter artist ID: ")
        
        if artist_id: 
            ratings_data = {
                "rating_id": int(rating_id),
                "song_id": int(song_id),
                "user_id": int(user_id),
                "rating_value": int(rating_value),
                "comment": comment,
                "date_rated": date_rated,
                "artist_id": int(artist_id),
            }

            data=data.append(ratings_data,ignore_index=True)
            st.subheader("Updated table")
            st.table(data)
elif app_mode=="Update":
    column_to_update = st.selectbox("Choose the column to update",table_columns[table])
    prev_value=st.text_input("Enter previous value: ",key="a1")
    if prev_value:
        id_value=data[data[column_to_update]==prev_value].index[0]
        if str(data[column_to_update].dtype)=="int64":
            update_value = st.text_input("Enter update value: ",key="a3")
            if update_value:
                st.success("Since multiple values found only first index value get updated")
                data.at[id_value, column_to_update] = int(update_value)
                st.subheader("Updated table")
                st.table(data)
        else:
            update_value = st.text_input("Enter update value: ",key="a4")
            if update_value:
                st.success("Since multiple values found only first index value get updated")
                data.at[id_value, column_to_update] = update_value
                st.subheader("Updated table")
                st.table(data)

    # OLAP Functionality
elif app_mode == "OLAP":
    st.subheader("OLAP Functionality")

    # Group by columns
    cols = st.multiselect("Select columns to group by:", table_columns[table])
    if cols:
        group_by_data = data.groupby(cols).size().reset_index(name='count')
        st.subheader("Grouped Data")
        st.table(group_by_data)

    # Apply aggregate functions
    agg_functions = ["mean", "sum", "min", "max"]
    selected_functions = st.multiselect("Select aggregate functions:", agg_functions)
    selected_cols = st.multiselect("Select columns to apply aggregate functions:", table_columns[table])
    if selected_functions and selected_cols:
        agg_data = data[selected_cols].agg(selected_functions)
        st.subheader("Aggregate Data")
        st.table(agg_data)

    # Pivot Table Functionality
elif app_mode == "Pivot":
    st.subheader("Pivot Table Functionality")

    # Select pivot index, columns, and values
    index_col = st.selectbox("Select index column:", table_columns[table])
    pivot_col = st.selectbox("Select pivot column:", table_columns[table])
    value_col = st.selectbox("Select value column:", table_columns[table])

    if index_col and pivot_col and value_col:
        # Create pivot table
        pivot_table = data.pivot_table(index=index_col, columns=pivot_col, values=value_col, aggfunc='sum')

        st.subheader("Pivot Table")
        st.table(pivot_table)
    
    # Drill Down Functionality
elif app_mode == "Drill Down":
    st.subheader("Drill Down Functionality")

    # Select drill down column
    drill_down_col = st.selectbox("Select column to drill down:", table_columns[table])

    if drill_down_col:
        # Filter data based on drill down column
        filtered_data = data[data[drill_down_col].notnull()]

        st.subheader("Drilled Down Data")
        st.table(filtered_data)

    # Roll Up Functionality
elif app_mode == "Roll Up":
    st.subheader("Roll Up Functionality")

    # Select roll up column
    roll_up_col = st.selectbox("Select column to roll up:", table_columns[table])

    if roll_up_col:
        # Group data based on roll up column
        rolled_up_data = data.groupby(roll_up_col).sum()

        st.subheader("Rolled Up Data")
        st.table(rolled_up_data)

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

        st.subheader("Diced Data")
        st.table(diced_data)

    # Slice Functionality
elif app_mode == "Slice":
    st.subheader("Slice Functionality")

    # Select slice column and value
    slice_col = st.selectbox("Select column to slice:", table_columns[table])
    slice_value = st.text_input("Enter value to slice:")

    if slice_col and slice_value:
        # Filter data based on slice column and value
        sliced_data = data[data[slice_col] == slice_value]

        st.subheader("Sliced Data")
        st.table(sliced_data)
        
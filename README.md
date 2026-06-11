# Music Application — CRUD + OLAP

> A Streamlit web application for managing a music database with full CRUD operations and OLAP analytics. Built with Python, SQLite, and Pandas.

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red) ![SQLite](https://img.shields.io/badge/SQLite-3-green)

---

## Features

### CRUD Operations
- **View** — Browse any table with live statistics and bar charts
- **Insert** — Add records to any table with type-safe input forms
- **Update** — Edit any field by ID with automatic type casting
- **Delete** — Remove records by primary key with live confirmation

### OLAP Analytics
- **Aggregate** — GROUP BY with count, mean, sum, min, max across any columns
- **Pivot Table** — Cross-tabulate any two dimensions with numeric aggregation
- **Slice** — Filter the dataset by a single column value
- **Dice** — Select any subset of columns to view
- **Roll Up** — Summarise numeric data grouped by a dimension
- **Drill Down** — Filter to non-null values with keyword search

---

## Database Schema

10 related tables forming a complete music domain model:

| Table | Description |
|---|---|
| `user` | Platform users |
| `artist` | Music artists |
| `song` | Individual songs |
| `album` | Artist albums |
| `chords` | Guitar/music chords |
| `playlist` | User playlists |
| `gener` | Music genres |
| `lyric` | Song lyrics with language |
| `instrument` | Instruments per artist |
| `ratings` | User ratings and reviews |

---

## Quick Start

```bash
# Clone
git clone https://github.com/mrunaliyadav003/Music-Application-Using-CRUD-and-OLAP.git
cd Music-Application-Using-CRUD-and-OLAP

# Install dependencies
pip install streamlit pandas

# Run
streamlit run gui.py
```

The app opens at `http://localhost:8501`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python 3 |
| Database | SQLite |
| Data layer | Pandas |

---

## Project Structure

```
Music-Application-Using-CRUD-and-OLAP/
├── gui.py                # Main Streamlit application
├── db_creation.py        # Database schema and seed data
├── music_db_final.db     # SQLite database
└── README.md
```

---

*Part of the Python/Data portfolio at [github.com/mrunaliyadav003](https://github.com/mrunaliyadav003)*

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "nss.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        college_name TEXT DEFAULT 'Your College Name',
        nss_unit TEXT DEFAULT 'NSS Unit',
        programme_officer TEXT DEFAULT '',
        academic_year TEXT DEFAULT '2026-27'
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS volunteers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        enrollment_no TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        class_name TEXT,
        division TEXT,
        mobile TEXT,
        email TEXT,
        joining_date TEXT,
        active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_code TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        activity_type TEXT NOT NULL,
        activity_date TEXT NOT NULL,
        start_time TEXT,
        end_time TEXT,
        venue TEXT,
        objectives TEXT,
        description TEXT,
        coordinator TEXT,
        beneficiaries INTEGER DEFAULT 0,
        status TEXT DEFAULT 'Planned',
        academic_year TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_id INTEGER NOT NULL,
        volunteer_id INTEGER NOT NULL,
        present INTEGER DEFAULT 1,
        hours REAL DEFAULT 0,
        UNIQUE(activity_id, volunteer_id),
        FOREIGN KEY(activity_id) REFERENCES activities(id) ON DELETE CASCADE,
        FOREIGN KEY(volunteer_id) REFERENCES volunteers(id) ON DELETE CASCADE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_id INTEGER NOT NULL,
        document_type TEXT NOT NULL,
        file_name TEXT NOT NULL,
        file_path TEXT NOT NULL,
        uploaded_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(activity_id) REFERENCES activities(id) ON DELETE CASCADE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_id INTEGER NOT NULL,
        particular TEXT NOT NULL,
        amount REAL DEFAULT 0,
        notes TEXT,
        FOREIGN KEY(activity_id) REFERENCES activities(id) ON DELETE CASCADE
    )
    """)

    cur.execute("INSERT OR IGNORE INTO settings (id) VALUES (1)")
    conn.commit()
    conn.close()

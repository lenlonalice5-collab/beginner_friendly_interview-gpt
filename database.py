import sqlite3

def init_db():

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        job TEXT,

        skill TEXT,

        question TEXT,

        answer TEXT,

        score INTEGER,

        create_time DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        total_score INTEGER DEFAULT 0,

        interview_count INTEGER DEFAULT 0,

        create_time DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mistakes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        question TEXT,

        answer TEXT,

        score INTEGER
    )
    """)

    conn.commit()

    conn.close()

def save_record(data):

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO interviews
    (
        job,
        skill,
        question,
        answer,
        score
    )

    VALUES

    (
        ?,
        ?,
        ?,
        ?,
        ?
    )
    """,

    (
        data["job"],
        data["skill"],
        data["question"],
        data["answer"],
        data["score"]
    )
    )

    conn.commit()

    conn.close()

def create_user(username):

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users(
        username
    )
    VALUES(?)
    """,
    (username,)
    )

    conn.commit()

    conn.close()

def get_all_records():

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM interviews
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_scores():

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT score
    FROM interviews
    """)

    rows = cursor.fetchall()

    conn.close()

    return [
        row[0]
        for row in rows
    ]

def get_user(username):

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM users
    WHERE username=?
    """,
    (username,)
    )

    row = cursor.fetchone()

    conn.close()

    return row

def update_user_score(
    username,
    score
):

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users
    SET

    total_score =
        total_score + ?,

    interview_count =
        interview_count + 1

    WHERE username=?
    """,

    (
        score,
        username
    )
    )

    conn.commit()

    conn.close()


def get_user_profile(username):

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    username,
    total_score,
    interview_count
    FROM users
    WHERE username=?
    """,
    (username,)
    )

    row = cursor.fetchone()

    conn.close()

    return row

def get_leaderboard():

    conn = sqlite3.connect(
        "interview.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        username,
        total_score,
        interview_count
    FROM users

    WHERE interview_count > 0

    ORDER BY
    CAST(total_score AS FLOAT)
    /
    interview_count DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows
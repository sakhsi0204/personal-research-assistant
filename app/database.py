import sqlite3

DB_NAME = "database/research_papers.db"


def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS papers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        authors TEXT,
        pdf_path TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database Created Successfully")


def insert_paper(title, authors, pdf_path):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO papers
        (title, authors, pdf_path)
        VALUES (?, ?, ?)
        """,
        (title, authors, pdf_path)
    )

    conn.commit()
    conn.close()

    print("Paper Saved")


def view_papers():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM papers")

    records = cursor.fetchall()

    conn.close()

    return records
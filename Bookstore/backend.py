import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS catalog
        (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)""")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    isbn = str(isbn)
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO catalog VALUES (NULL, ?, ?, ?, ?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM catalog")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    isbn = str(isbn)
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM catalog WHERE title=? OR author=? pr year=? or isbn=?",
                (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM catalog WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    isbn = str(isbn)
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE catalog SET title=?, author =?, year=?, isbn=? WHERE id=?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()

from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    return conn

# Home Page
@app.route("/")
def home():
    return {
        "message": "Hello Backend!"
    }

# Get All Books

@app.route("/books")
def get_all_books():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    conn.close()

    return {
        "books": [dict(book) for book in books]
    }

#Get Book By ID

@app.route("/books/<int:book_id>")
def get_book_by_id(book_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM books WHERE book_id = ?",
        (book_id,)
    )

    book = cursor.fetchone()

    conn.close()

    if book:
        return {"book": dict(book)}

    return {
        "Error": "Book not found"
    },404

#Get Book By Author

@app.route("/author/<string:author>")
def get_book_by_author(author):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM books WHERE author LIKE ?",
        ('%' + author + '%',)
    )

    books = cursor.fetchall()

    conn.close()

    if books:
        return {
            "books": [dict(book) for book in books]
        }

    return {
        "Error": "No books found"
    },404

#Get Book By Title

@app.route("/title/<string:title>")
def get_book_by_title(title):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
    "SELECT * FROM books WHERE title LIKE ?",
    ('%' + title + '%',)
     )

    books = cursor.fetchall()

    conn.close()

    if books:
     return {
        "books": [dict(book) for book in books]
      }

    return {
        "Error": "No Books found"
    },404

#CREATE Books

@app.route("/books", methods=["POST"])
def add_book():

    data = request.get_json()

    required_fields = [
    "title",
    "author",
    "genre",
    "publication_year",
    "availability"
    ]

    for field in required_fields:
     if field not in data:
        return {
            "Error": f"{field} is required"
        },400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            INSERT INTO books
            (title, author, genre, publication_year, availability)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data["title"],
            data["author"],
            data["genre"],
            data["publication_year"],
            data["availability"]
        ))

        conn.commit()

        return {
            "message": "Book added successfully"
        },201

    except sqlite3.IntegrityError:

     return {
        "Error": "Database error"
      },409

    finally:
        conn.close()

#Update Book

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):

    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE books
        SET title=?,
            author=?,
            genre=?,
            publication_year=?,
            availability=?
        WHERE book_id=?
    """, (
        data["title"],
        data["author"],
        data["genre"],
        data["publication_year"],
        data["availability"],
        book_id
    ))

    rows_updated = cursor.rowcount

    conn.commit()
    conn.close()

    if rows_updated == 0:
        return {
            "Error": "Book not found"
        },404

    return {
        "message": "Book updated successfully"
    }

#Delete Book

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM books WHERE book_id = ?",
        (book_id,)
    )

    rows_deleted = cursor.rowcount

    conn.commit()
    conn.close()

    if rows_deleted == 0:
        return {
            "Error": "Book not found"
        },404

    return {
        "message": "Book deleted successfully"
    }

#Available Books route

@app.route("/available-books")
def get_available_books():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM books WHERE availability = ?",
        (True,)
    )

    books = cursor.fetchall()

    conn.close()

    return {
        "books": [dict(book) for book in books]
    }


if __name__ == "__main__":
    app.run(debug=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
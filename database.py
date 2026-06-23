import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

#structured created
cursor.execute("""                
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    genre TEXT,
    publication_year INTEGER,
    availability BOOLEAN
)
""")

#Data Added ,Library Books Data
books = [
    (1001, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 1997, True),
    (1002, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Fantasy", 1998, True),
    (1003, "The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, True),
    (1004, "The Lord of the Rings", "J.R.R. Tolkien", "Fantasy", 1954, False),
    (1005, "Percy Jackson and the Lightning Thief", "Rick Riordan", "Fantasy", 2005, True),

    (1006, "Sherlock Holmes", "Arthur Conan Doyle", "Mystery", 1892, True),
    (1007, "Murder on the Orient Express", "Agatha Christie", "Mystery", 1934, True),
    (1008, "Gone Girl", "Gillian Flynn", "Mystery", 2012, False),
    (1009, "The Silent Patient", "Alex Michaelides", "Mystery", 2019, True),
    (1010, "The Girl with the Dragon Tattoo", "Stieg Larsson", "Mystery", 2005, True),

    (1011, "The Da Vinci Code", "Dan Brown", "Thriller", 2003, True),
    (1012, "Angels and Demons", "Dan Brown", "Thriller", 2000, True),
    (1013, "The Bourne Identity", "Robert Ludlum", "Thriller", 1980, False),
    (1014, "Jurassic Park", "Michael Crichton", "Thriller", 1990, True),
    (1015, "The Hunt for Red October", "Tom Clancy", "Thriller", 1984, True),

    (1016, "Pride and Prejudice", "Jane Austen", "Romance", 1813, True),
    (1017, "Me Before You", "Jojo Moyes", "Romance", 2012, True),
    (1018, "The Notebook", "Nicholas Sparks", "Romance", 1996, False),
    (1019, "It Ends With Us", "Colleen Hoover", "Romance", 2016, True),
    (1020, "The Fault in Our Stars", "John Green", "Romance", 2012, True),

    (1021, "Atomic Habits", "James Clear", "Self-Help", 2018, True),
    (1022, "The Power of Habit", "Charles Duhigg", "Self-Help", 2012, True),
    (1023, "Think and Grow Rich", "Napoleon Hill", "Self-Help", 1937, True),
    (1024, "The 7 Habits of Highly Effective People", "Stephen Covey", "Self-Help", 1989, False),
    (1025, "Rich Dad Poor Dad", "Robert Kiyosaki", "Self-Help", 1997, True),

    (1026, "Steve Jobs", "Walter Isaacson", "Biography", 2011, True),
    (1027, "Wings of Fire", "A.P.J. Abdul Kalam", "Biography", 1999, True),
    (1028, "Long Walk to Freedom", "Nelson Mandela", "Biography", 1994, False),
    (1029, "The Diary of a Young Girl", "Anne Frank", "Biography", 1947, True),
    (1030, "Becoming", "Michelle Obama", "Biography", 2018, True),

    (1031, "Dune", "Frank Herbert", "Science Fiction", 1965, True),
    (1032, "The Martian", "Andy Weir", "Science Fiction", 2011, True),
    (1033, "Foundation", "Isaac Asimov", "Science Fiction", 1951, True),
    (1034, "Ready Player One", "Ernest Cline", "Science Fiction", 2011, False),
    (1035, "Ender's Game", "Orson Scott Card", "Science Fiction", 1985, True),

    (1036, "C Programming Language", "Dennis Ritchie", "Programming", 1978, True),
    (1037, "Python Crash Course", "Eric Matthes", "Programming", 2019, True),
    (1038, "Clean Code", "Robert C. Martin", "Programming", 2008, True),
    (1039, "Head First Java", "Kathy Sierra", "Programming", 2003, False),
    (1040, "JavaScript: The Good Parts", "Douglas Crockford", "Programming", 2008, True)
]


cursor.executemany("""
INSERT OR REPLACE INTO books
VALUES (?, ?, ?, ?, ?, ?)
""", books)
print("Books inserted successfully")


conn.commit()
conn.close()


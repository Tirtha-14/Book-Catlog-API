# Book Catalog API

## Project Description

This project is a backend application developed using Flask and SQLite. It allows users to manage a library book catalog through REST API endpoints.

## Features

* Add a new book
* View all books
* View a book by ID
* Search books by title
* Search books by author
* Update book details
* Delete a book
* Check available books
* Input validation
* Error handling
* Auto-increment book IDs

## Technologies Used

* Python
* Flask
* SQLite
* Postman

## API Endpoints

### GET

* /books
* /books/<book_id>
* /title/<title>
* /author/<author>
* /available-books

### POST

* /books

### PUT

* /books/<book_id>

### DELETE

* /books/<book_id>

## Database

The project uses SQLite database (library.db) for storing book information.

## Author

Tirtha Mogarkar

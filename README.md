# Book Library API

A RESTful Book Library API built using FastAPI and PostgreSQL. The API provides complete CRUD operations for managing books and uses SQLModel for database interaction.

## Features

- Create a new book
- Get all books
- Get a book by ID
- Update a book
- Delete a book
- PostgreSQL database integration
- Data validation using SQLModel
- Error handling for non-existing books
- Environment variables for database credentials

## Technologies Used

- Python
- FastAPI
- SQLModel
- PostgreSQL
- Psycopg
- Uvicorn
- python-dotenv

## Book Fields

Each book contains:

- ID
- Title
- Author
- Category
- Price
- Availability

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/books` | Create a new book |
| GET | `/books` | Get all books |
| GET | `/books/{book_id}` | Get a book by ID |
| PUT | `/books/{book_id}` | Update a book |
| DELETE | `/books/{book_id}` | Delete a book |

## Database

The project uses PostgreSQL as the database.

Database credentials are stored in a `.env` file and are excluded from GitHub using `.gitignore`.

## How to Run

1. Clone the repository.

2. Create and activate a virtual environment.

3. Install the required dependencies:

```bash
pip install -r requirements.txt

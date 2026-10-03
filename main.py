from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import URL  
from sqlmodel import SQLModel, Field, Session, create_engine, select

import os
from dotenv import load_dotenv

load_dotenv() 



app = FastAPI()


# Database URL
DATABASE_URL = URL.create(
    "postgresql+psycopg",
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

engine = create_engine(DATABASE_URL, echo=True)


# Table
class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    author: str
    category: str
    price: float
    available: bool
    
SQLModel.metadata.create_all(engine)


# Session
def get_session():
    with Session(engine) as session:
        yield session


# CREATE
@app.post("/books")
def create_book(
    book: Book,
    session: Session = Depends(get_session)
):
    session.add(book)
    session.commit()
    session.refresh(book)

    return book
@app.get("/books")
def get_books(session: Session = Depends(get_session)):
    books = session.exec(select(Book)).all()
    return books
@app.get("/books/{book_id}")
def get_book_by_id(book_id:int, session:Session = Depends(get_session)):
    book = session.get(Book,book_id)
    if book is None  :
        raise HTTPException(status_code=404,detail="book not found")
    return book
@app.put("/books/{book_id}")
def update_book(book_id:int , updated_book: Book, session :Session = Depends(get_session)):  
    book = session.get(Book,book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="book not found")
    book.title = updated_book.title
    book.author = updated_book.author   
    book.category = updated_book.category   
    book.price = updated_book.price 
    book.available = updated_book.available 
    session.add(book)
    session.commit()
    session.refresh(book)
    return book 
@app.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):

    book = session.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="book not found"
        )

    session.delete(book)
    session.commit()

    return {"message": "Book deleted successfully"}
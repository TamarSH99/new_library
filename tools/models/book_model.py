from flask_sqlalchemy import SQLAlchemy
from .read_books_model import ReadBooks
from config import db


class Book(db.Model):
    __tablename__ = 'book'
    book_isbn = db.Column(db.Text, primary_key=True)
    book_authors = db.Column(db.Text)
    book_desc = db.Column(db.Text)
    book_edition = db.Column(db.Text)
    book_format = db.Column(db.Text)
    book_pages = db.Column(db.Integer)
    book_rating = db.Column(db.Float)
    book_rating_count = db.Column(db.Integer)
    book_review_count = db.Column(db.Integer)
    book_title = db.Column(db.Text)
    genres = db.Column(db.Text)
    image_url = db.Column(db.Text)


    def general_info(self):
        return Book.query.all()
    
    def find_by_author_or_title(cls, author_or_title=None):
        if author_or_title:
            return Book.query.filter((Book.book_authors.ilike(f'%{author_or_title}%')) | (Book.book_title.ilike(f'%{author_or_title}%'))).all()
        else:
            return []

    def get_read_books_info(user_id):
        book_info = []
        read_books_id = ReadBooks.get_books_by_user(user_id)
        for id in read_books_id:
            book = Book.query.filter(Book.book_isbn.ilike(f'%{id}%')).first()
            if book:
                book_info.append(book)
        return book_info



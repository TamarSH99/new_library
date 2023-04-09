from flask_sqlalchemy import SQLAlchemy
from config import db

class ReadBooks(db.Model):
    __tablename__ = 'read_books'
    user_id = db.Column(db.Integer, primary_key=True)
    book_isbn = db.Column(db.Text, primary_key=True)

    @staticmethod
    def add_book_to_user(user_id, book_isbn):
        new_book = ReadBooks(user_id=user_id, book_isbn=book_isbn)
        db.session.add(new_book)
        db.session.commit()

    def get_books_by_user(user_id):
        books = ReadBooks.query.filter_by(user_id=user_id).all()
        book_ids = [book.book_isbn for book in books]
        return book_ids
   

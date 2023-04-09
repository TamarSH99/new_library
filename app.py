from flask import Flask, render_template, url_for, redirect, session, request, jsonify, Blueprint
from flask_login import  LoginManager, logout_user, login_required
import logging

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import json
# import forms
from tools.forms.general_register_form import GeneralRegisterForm
from tools.forms.login_form import LoginForm
from tools.forms.only_user_register_form  import OnlyUserRegisterForm
# import models
from tools.models.user_model import  User
from tools.models.book_model import  Book
from tools.models.read_books_model import ReadBooks
from config import db, db_map

app = Flask(__name__)

file_handler = logging.FileHandler('library.log')
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)

app.config['SQLALCHEMY_DATABASE_URI'] = db_map['SQLALCHEMY_DATABASE_URI']
app.config['SECRET_KEY'] = db_map['SECRET_KEY']
db.init_app(app)


admin = Admin(app)
admin_bp = Blueprint('admin', __name__)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@admin_bp.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    print(session['user_id'].is_administrator())
    if not session['user_id'].is_administrator():
        return redirect(url_for('dashboard'))
    
    form = GeneralRegisterForm()  
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data, is_admin=form.is_admin.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('admin_bp.admin'))
    
    users = User.query.all()
    return render_template('admin.html', form=form, users=users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in  session:
        return redirect(url_for('dashboard'))
    
    form = OnlyUserRegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and form.check_account():
        user = User.query.filter_by(username=form.username.data).first()
        session['user_id'] = user.user_id
        if user.is_administrator():
            return redirect(url_for('admin_bp.admin'))
        return redirect(url_for('dashboard'))
    
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    app.logger.warning('User %s logout ', session['user_id'])
    logout_user()
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET'])
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    
    search_query = request.args.get('search', '')
    if search_query:
        books= Book().find_by_author_or_title(search_query)
    else:
        books =Book().general_info()
    return render_template('home.html', books=books)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    app.logger.warning('User %s accessed the dashboard', session['user_id'])

    read_books = ReadBooks.get_books_by_user(user_id=session.get('user_id'))

    if request.method == 'POST':
        data = json.loads(request.data)
        ReadBooks.add_book_to_user(user_id=session.get('user_id'), book_isbn=data['book_id'])
        read_books = ReadBooks.get_books_by_user(user_id=session.get('user_id'))
        all_books = Book().general_info() 
        return render_template("dashboard.html", books=all_books, read_books_isbn=read_books)
    

    if request.method == 'GET':
        search_query = request.args.get('search', '')
        if search_query:
            books = Book().find_by_author_or_title(search_query)
        elif request.args.get('read-books') == 'true':
            books = Book.get_read_books_info(user_id=session.get('user_id'))
        else:
            books = Book().general_info()       
        return render_template("dashboard.html", books=books, read_books_isbn=read_books)


@app.route('/find_your_book')
def find_your_book():
    return render_template("find_your_book.html")



if __name__ == "__main__":
    app.run(debug=True)
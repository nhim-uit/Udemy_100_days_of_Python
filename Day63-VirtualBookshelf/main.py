# Udemy: Master Python by building 100 projects in 100 days
# Mar 02, 2025
# Day 63 - Virtual Bookshelf project
# Created by me (Alex Mai)

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms.fields import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
# import sqlite3

# db = sqlite3.connect('books-collection.db', check_same_thread=False)
# cursor = db.cursor()
#
# cursor.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, '
#                'title varchar(250) NOT NULL UNIQUE, '
#                'author varchar(250) NOT NULL, rating FLOAT NOT NULL)')


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# create app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde'
Bootstrap5(app)

# configure the SQLite db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
# initialize the app
db.init_app(app)

# all_books = []


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book', validators=[DataRequired()])


class RatingForm(FlaskForm):
    rating = FloatField('New Rating', validators=[DataRequired()])
    submit = SubmitField('Change Rating', validators=[DataRequired()])


# create table schema in the db
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()

    return render_template('index.html', all_books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookForm()

    if form.validate_on_submit():
        # using dictionary
        # all_books.append({
        #     'title': form.name.data,
        #     'author': form.author.data,
        #     'rating': form.rating.data,
        # })

        # using sqlite db
        # cursor.execute('INSERT INTO books (title, author, rating) VALUES (?, ?, ?)',
        #                (form.name.data, form.author.data, form.rating.data))
        # db.commit()
        book = Book(
            title=form.name.data,
            author=form.author.data,
            rating=form.rating.data,
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    form = RatingForm()
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()

    if form.validate_on_submit():
        book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, book=book)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')

    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

# Udemy: Master Python by building 100 projects in 100 days
# Mar 02, 2025
# Day 63 - Virtual Bookshelf project
# Created by me (Alex Mai)

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import sqlite3

db = sqlite3.connect('books-collection.db', check_same_thread=False)
cursor = db.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, '
               'title varchar(250) NOT NULL UNIQUE, '
               'author varchar(250) NOT NULL, rating FLOAT NOT NULL)')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde'
Bootstrap5(app)

# all_books = []


class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book', validators=[DataRequired()])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookForm()

    if form.validate_on_submit():
        # all_books.append({
        #     'title': form.name.data,
        #     'author': form.author.data,
        #     'rating': form.rating.data,
        # })
        cursor.execute('INSERT INTO books (title, author, rating) VALUES (?, ?, ?)',
                       (form.name.data, form.author.data, form.rating.data))
        db.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

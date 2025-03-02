# Udemy: Master Python by building 100 projects in 100 days
# Mar 02, 2025
# Day 63 - Virtual Bookshelf project
# Created by me (Alex Mai)

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

app = Flask('__name__')
app.config['SECRET_KEY'] = 'abcde'
Bootstrap5(app)

all_books = []


class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book', validators=[DataRequired()])


@app.route('/')
def home():
    return render_template('index.html', all_books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookForm()

    if form.validate_on_submit():
        all_books.append({
            'title': form.name.data,
            'author': form.author.data,
            'rating': form.rating.data,
        })
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

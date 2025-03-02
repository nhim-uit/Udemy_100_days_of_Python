# Udemy: Master Python by building 100 projects in 100 days
# Mar 02, 2025
# Day 63 - Virtual Bookshelf project
# Created by me (Alex Mai)

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask('__name__')
app.config['SECRET_KEY'] = 'abcde'
Bootstrap5(app)

class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book', validators=[DataRequired()])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add')
def add():
    form = BookForm()

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

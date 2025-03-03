# Udemy: Master Python by building 100 projects in 100 days
# Mar 02, 2025
# Day 64 - My Top 10 Movies
# Completed by me (Alex Mai)

from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, Float
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from wtforms.fields.numeric import FloatField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired


class Base(DeclarativeBase):
    pass


# Database
db = SQLAlchemy(model_class=Base)


# Create app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde(*&*%$JGJKYJK9876'
Bootstrap5(app)

# configure the SQLite db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
# initialize the app
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)


class RatingForm(FlaskForm):
    rating = FloatField('Rating out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    movies = db.session.execute(db.select(Movie)).scalars().all()
    return render_template('index.html', movies=movies)


@app.route('/add')
def add():
    new_movie = Movie(
        title='Phone Both',
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
    )

    second_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )
    db.session.add(new_movie)
    db.session.add(second_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = RatingForm()
    movie_id = request.args.get('id')
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()

    if form.validate_on_submit():
        movie.rating = request.form['rating']
        movie.review = request.form['review']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie)


if __name__ == '__main__':
    app.run(debug=True)

# Udemy: Master Python by building 100 projects in 100 days
# Apr 1, 2025
# Day 69 - Blog Capstone - Added Authentication with User
# Completed by me (Alex Mai)

import datetime

from flask import Flask, render_template, request, redirect, url_for
from flask_ckeditor import CKEditorField, CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_bootstrap import Bootstrap5
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdsadkjgh976897asd'
ckeditor = CKEditor(app)
Bootstrap5(app)


# Create database
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(blog_id):
    return db.get_or_404(blog_post, blog_id)


# CONFIGURE TABLE
class blog_post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# FORM
class PostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    name = StringField('Your Name', validators=[DataRequired()])
    url = StringField('Blog Image URL', validators=[DataRequired()])
    content = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(blog_post)).scalars().all()
    return render_template("index.html", posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/post')
def show_post():
    post_id = request.args.get('id')
    requested_post = db.get_or_404(blog_post, int(post_id))
    if requested_post:
        return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    form = PostForm()

    if form.validate_on_submit():
        post = blog_post(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=datetime.datetime.now().strftime('%B %d, %Y'),
            body=form.content.data,
            author=form.name.data,
            img_url=form.url.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)


# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<id>', methods=['GET', 'POST'])
def edit(id):
    post = db.get_or_404(blog_post, id)
    edit_form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        url=post.img_url,
        author=post.author,
        content=post.body,
        name=post.author,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.url.data
        post.body = edit_form.content.data
        post.author = edit_form.name.data
        db.session.commit()
        return redirect(url_for('show_post', id=post.id))
    return render_template('make-post.html', form=edit_form, is_edit=True)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<id>')
def delete(id):
    post = db.get_or_404(blog_post, id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)

# Udemy: Master Python by building 100 projects in 100 days
# Apr 1, 2025
# Day 69 - Blog Capstone - Added Authentication with User
# Completed by me (Alex Mai)

import datetime
from functools import wraps

import werkzeug
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_ckeditor import CKEditorField, CKEditor
from flask_gravatar import Gravatar
from flask_login import LoginManager, login_user, UserMixin, current_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from flask_bootstrap import Bootstrap5
from werkzeug.security import check_password_hash
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
def load_user(user_id):
    return db.session.get(User, user_id)


# admin only
def admin_only(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return wrapper


# gravatar
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# TABLE User
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    comments = relationship('Comment', back_populates='user')
    blogs = relationship('blog_post', back_populates='author')


# CONFIGURE FLASK-WTF FORM
# TABLE blog_post
class blog_post(db.Model):
    __tablename__ = 'blog_post'
    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    author_id: Mapped[str] = mapped_column(Integer, db.ForeignKey('users.id'))
    author = relationship('User', back_populates='blogs')
    comments = relationship('Comment', back_populates='blog')


# TABLE Comment
class Comment(db.Model):
    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    comment: Mapped[str] = mapped_column(String(1000))

    user_id: Mapped[str] = mapped_column(Integer, db.ForeignKey('users.id'))
    user = relationship('User', back_populates='comments')

    blog_id: Mapped[str] = mapped_column(Integer, db.ForeignKey('blog_post.id'))
    blog = relationship('blog_post', back_populates='comments')


with app.app_context():
    db.create_all()


# POST FORM
class PostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    name = StringField('Your Name', validators=[DataRequired()])
    url = StringField('Blog Image URL', validators=[DataRequired()])
    content = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


class CommentForm(FlaskForm):
    comment_ = CKEditorField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(blog_post)).scalars().all()
    admin = current_user.is_authenticated and current_user.id == 1
    return render_template("index.html", posts=posts, logged_in=current_user.is_authenticated, admin=admin)


# TODO: Add a route so that you can click on individual posts.
@app.route('/post', methods=['GET', 'POST'])
def show_post():
    post_id = request.args.get('id')
    requested_post = db.get_or_404(blog_post, post_id)
    comment_ = CommentForm()

    if comment_.validate_on_submit():
        cmt = Comment(
            comment=comment_.comment_.data,
            user_id=current_user.id,
            blog_id=post_id,
        )
        db.session.add(cmt)
        db.session.commit()
        comments = db.session.execute(db.select(Comment)).scalars().all()
        return render_template('post.html',
                               post=requested_post,
                               comment_=comment_,
                               comments=comments,
                               logged_in=current_user.is_authenticated)

    if requested_post:
        comments = db.session.execute(db.select(Comment)).scalars().all()
        return render_template("post.html",
                               post=requested_post,
                               comment_=comment_,
                               comments=comments,
                               logged_in=current_user.is_authenticated)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
@admin_only
def add_new_post():
    form = PostForm(
        name=current_user.name,
    )

    if form.validate_on_submit():
        post = blog_post(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=datetime.datetime.now().strftime('%B %d, %Y'),
            body=form.content.data,
            img_url=form.url.data,
            author_id=current_user.id,
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=form, logged_in=current_user.is_authenticated)


# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<id>', methods=['GET', 'POST'])
@admin_only
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

    return render_template('make-post.html',
                           form=edit_form,
                           is_edit=True,
                           logged_in=current_user.is_authenticated)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<id>')
@admin_only
def delete(id):
    post = db.get_or_404(blog_post, id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts', logged_in=current_user.is_authenticated))


@app.route('/delete-comment')
@login_required
def delete_comment():
    comment_id = request.args.get('comment_id')
    post_id = request.args.get('id')
    # requested_post = db.get_or_404(blog_post, post_id)

    # TODO
    # only delete if user id match user currently logged in
    # user = request.args.get('user')

    comment = db.get_or_404(Comment, comment_id)
    db.session.delete(comment)
    db.session.commit()

    # if requested_post:
    return redirect(url_for('show_post', id=post_id))


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            user = db.session.execute(db.select(User).where(User.email == email)).scalar()

            if not user:
                flash('Invalid email, please try again!')
            else:
                if not check_password_hash(user.password, password):
                    flash('Invalid password, please try again!')
                else:
                    login_user(user)
                    return redirect(url_for('get_all_posts'))

        except Exception as e:
            flash('An error occurred while trying to log in', str(e))

    return render_template('login.html', logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        res = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if res:
            flash('Account with that email already exists, please log in or use different email!')
        else:
            new_user = User(
                email=email,
                password=werkzeug.security.generate_password_hash(
                    request.form.get('password'),
                    method='pbkdf2:sha256',
                    salt_length=8),
                name=request.form.get('name')
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            return redirect(url_for('get_all_posts', logged_in=current_user.is_authenticated))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts',logged_in=current_user.is_authenticated))


if __name__ == "__main__":
    app.run(debug=True)

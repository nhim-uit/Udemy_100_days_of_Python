# Udemy: Master Python by building 100 projects in 100 days
# Feb 12, 2025
# Day 57 - Blog Capstone Project
# Create by me (Alex Mai)

from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/blog')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template('index.html', posts=all_posts)


@app.route('/post/<blog_id>')
def get_blog(blog_id):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()

    post_title = post_subtitle = post_body = None

    for i in all_posts:
        if i['id'] == int(blog_id):
            post_title = i['title']
            post_subtitle = i['subtitle']
            post_body = i['body']

    if not post_title:
        return 'Blog post not found', 404

    return render_template('blog.html',
                           title=post_title,
                           subtitle=post_subtitle,
                           body=post_body)


if __name__ == '__main__':
    app.run(debug=True)

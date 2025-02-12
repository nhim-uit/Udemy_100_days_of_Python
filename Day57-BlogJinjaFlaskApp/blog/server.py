# Udemy: Master Python by building 100 projects in 100 days
# Feb 12, 2025
# Day 57 - Templating with Jinja in Flask Application
# Multiline Statements with Jinja

from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'

    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)

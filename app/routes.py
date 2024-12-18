from flask import render_template, request
from app import app
from . import htmx
import logging

import os
import markdown
import frontmatter

from app.model.Post import Post

logging.basicConfig(level=logging.DEBUG)

def load_posts():
    posts = []
    for filename in os.listdir("app/posts"):
        if filename.endswith(".md"):
            try:
                with open(f"app/posts/{filename}", "r") as f:
                    post_data = frontmatter.load(f)

                id = post_data.get("id", "Unknown")
                title = post_data.get("title", "Unknown title")
                date = post_data.get("date", "Unknown date")
                content = markdown.markdown(post_data.content)

                post = Post(id, title, date, content)
                posts.append(post)
            except Exception as e:
                print(f"Error in {filename}: {e}")
    return posts


posts = load_posts()

@app.route("/")
@app.route("/index.html")
def index():
    logging.debug(f"Headers: {request.headers}")
    if request.headers.get("HX-Request"):
        logging.debug("HTMX request detected")
        return render_template("/partials/posts.html", posts=posts)
    
    logging.debug("Standard request")
    return render_template("index.html", posts=posts)


@app.route("/post/<int:postId>.html")
def showPost(postId):
    found = next((post for post in posts if post.id == postId))
    return render_template("/partials/post.html", post = found)

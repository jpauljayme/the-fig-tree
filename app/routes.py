from flask import render_template
from app import app

import os
import markdown
import frontmatter

from app.model.Post import Post


def load_posts():
    posts = []
    for filename in os.listdir("app/posts"):
        if filename.endswith(".md"):
            with open(f"app/posts/{filename}", "r") as f:
                post_data = frontmatter.load(f)

            id = post_data.get("id", "Unknown")
            print(type(id))
            title = post_data.get("title", "Unknown title")
            date = post_data.get("date", "Unknown date")
            content = markdown.markdown(post_data.content)

            post = Post(id, title, date, content)
            print(post)
            posts.append(post)

    return posts


posts = load_posts()

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:postId>")
def showPost(postId):
    print(f"id to find {postId} and type of {type(postId)}")
    found = next((post for post in posts if post.id == postId))
    return render_template("post.html", post = found)

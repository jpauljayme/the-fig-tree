from flask import render_template
from app import app

import os
import markdown
# /Users/johnpauljayme/personal-projects/microblog/app/routes.py
# /Users/johnpauljayme/personal-projects/microblog/app/posts
def load_posts():
	posts = []
	for filename in os.listdir('app/posts'):
		if filename.endswith('.md'):
			with open(f'app/posts/{filename}', 'r') as f:
				content = f.read()
				html_content = markdown.markdown(content)
				id = filename.split('.')[0]
				post = {
					'id': id,
					'content': html_content
				}
				posts.append(post)
	
	return posts

posts = load_posts()

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html', 
						posts=posts
					)

@app.route('/post')
def showPost(id):
	for post in posts:
		if post.id == id:
			return render_template('post.html',
						  post=post)


"""
Simple "Hello, World" application using Flask
"""

# from flask import Flask, url_for, request, render_template, abort, redirect
# from markupsafe import escape

# app = Flask(__name__)

# #Routing
# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello_world():
#     return 'Hello World!'

# #Variable Rules
# @app.route('/user/<username>')
# def show_user_profile(username):
#     #show user profile for that user
#     return 'User %s' % escape(username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     #show post with given id, id is integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     #show subpath after /path/
#     return 'Subpath %s' % escape(subpath)

# #Unique URLs / Redirection Behavior
# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# #URL Building
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{escape(username)}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

# #HTTP Methods
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

#Static Files
# url_for('static', filename='style.css')

#Rendering Templates
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
# #Case 1: a module
# #Case 2: a package

# #Redirects and Errors
# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     abort(401) #401 is access denied
#     this_is_never_executed()

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404

from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)
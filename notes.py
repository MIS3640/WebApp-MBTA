# Run the application with flask command or python's -m switch with flask
""" 
$ export FLASK_APP=mbta_webapp.py
$ flask run
 * Running on http://127.0.0.1:5000/
"""
# windows command prompt
""" 
C:\path\to\app>set FLASK_APP=hello.py
"""
# PowerShell
""" 
PS C:\path\to\app> $env:FLASK_APP = "hello.py"
"""
# python -m flask
"""
$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
 """
# externally visible server
""" 
$ flask run --host=0.0.0.0 
"""
# Invalid import name: if module incorrectly named get import error on start / or if debug enabled when navigate to application
# most common reason is a typo or did not create an app object

# Debug: enable all dev features including debug - set it to development before running server
""" 
$ set FLASK_ENV=development
$ flask run
"""
# control debug separate from environment
""" 
FLASK_DEBUG=1 
"""
# routing - can make parts of the url dynamic and attach multiple rules to a function
""" 
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
"""
# variable rules - variable sections to url by marking sections with <variable_name> => function uses as keyword arg - or converter to specify type of arg <converter:variable_name>
# converter types: string, int, float, path (like string but also accepts slashes), uuid
""" 
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
"""
# unique urls / redirection behavior
""" 
@app.route('/projects/')
def projects():
    return 'The project page'
# endpoint has trailing slash. If access the URL without trailing slash, flask redicts to canonical url with trailing slash

@app.route('/about')
def about():
    return 'The about page'
# It’s similar to the pathname of a file. Accessing the URL with a trailing slash produces a 404 “Not Found” error. 
# This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.
 """
# url building
""" 
# test_request_context() method to try out url_for(). test_request_context() tells Flask to behave as though it’s handling a request even while we use a Python shell.

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
"""
# http methods
# By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.
# If GET is present, Flask automatically adds support for the HEAD method and handles HEAD requests according to the HTTP RFC. Likewise, OPTIONS is automatically implemented for you.
""" 
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
"""
# static files
# Ideally your web server is configured to serve them for you, but during development Flask can do that as well. 
# Just create a folder called static in your package or next to your module and it will be available at /static on the application.
# To generate URLs for static files, use the special 'static' endpoint name:
""" 
url_for('static', filename='style.css')
# The file has to be stored on the filesystem as static/style.css.
 """
# rendering templates
# To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables 
# you want to pass to the template engine as keyword arguments. Here’s a simple example of how to render a template:
""" 
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name) 
"""
# Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:
""" 
# module
/application.py
/templates
    /hello.html
# package
/application
    /__init__.py
    /templates
        /hello.html
# For templates you can use the full power of Jinja2 templates. Head over to the official Jinja2 Template Documentation for more information.
# http://jinja.pocoo.org/docs/templates/
# example template
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
 """
#  Inside templates you also have access to the request, session and g 1 objects as well as the get_flashed_messages() function.
# Templates are especially useful if inheritance is used. If you want to know how that works, head over to the Template Inheritance pattern documentation. 
# Basically template inheritance makes it possible to keep certain elements on each page (like header, navigation and footer).

# Automatic escaping is enabled, so if name contains HTML it will be escaped automatically. If you can trust a variable and you know that it will be safe HTML 
# (for example because it came from a module that converts wiki markup to HTML) you can mark it as safe by using the Markup class or by using the |safe filter in the template. 
# Head over to the Jinja 2 documentation for more examples.

# Unsure what that g object is? It’s something in which you can store information for your own needs, check the documentation of that object (g) and the Using SQLite 3 with Flask for more information.


"""  
>>> from markupsafe import Markup
>>> Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
>>> Markup.escape('<blink>hacker</blink>')
Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')
>>> Markup('<em>Marked up</em> &raquo; HTML').striptags()
u'Marked up \xbb HTML'
"""

# Redirects and Errors
# To redirect a user to another endpoint, use the redirect() function; to abort a request early with an error code, use the abort() function:
""" 
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed() 
"""
# This is a rather pointless example because a user will be redirected from the index to a page they cannot access (401 means access denied) but it shows how that works.
# By default a black and white error page is shown for each error code. If you want to customize the error page, you can use the errorhandler() decorator:
""" 
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404 
"""
# Note the 404 after the render_template() call. This tells Flask that the status code of that page should be 404 which means not found. By default 200 is assumed which translates to: all went well.
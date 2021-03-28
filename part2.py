
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

import os
SECRET_KEY = "abcd"
app.config['SECRET_KEY'] = SECRET_KEY


#index page greeting
@app.route('/')
def greeting():
    # if name:
    #     return f"hello, {name}!"
    # return "Hello! Welcome to the site!"

    form = MyForm() 
    if request.method == 'POST' and form.validate(): 
        user = User(form.username.data) 
        db_session.add(user) 
        flash('The email address is'" +email+")
        return redirect(url_for('login')) 
    return render_template('signup.html', form=form) 

#form Code 
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, length

class MyForm(FlaskForm):
    """Contact form."""
    username = StringField(
        'Username',
        [DataRequired()]
    )
    
    body = TextField(
        'Message',
        [
            DataRequired()
        ]
    )
    
    submit = SubmitField('Submit')

# @app.route('/', methods = ['GET', 'POST'])
# def location(): 
    # form = MyForm() 
    # if request.method == 'POST' and form.validate(): 
    #     user = User(form.username.data) 
    #     db_session.add(user) 
    #     flash('The email address is'" +email+")
    #     return redirect(url_for('login')) 
    # return render_template('signup.html', form=form) 


@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data = form_data)

app.run(host='localhost', port=5000)






# data page
# @app.route('/mbta_station')


# ''' THe Flask backend withll dandle the request to POST/nearest_mbta. 
# Then app will render a mbta_station page fo rthe user"
# presenting nearest MBTA stop and whether it is wheelchair accesble. This step requires you to use code from part 1
# '''


# if __name__ == "__main__":
#     app.run()






# def post_request():
#     url = 
#     myobj = {'somekey': 'somevalue'}

#     x = request.ost(url, data = myobj)


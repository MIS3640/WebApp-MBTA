
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, length

app = Flask(__name__)

import os
SECRET_KEY = "abcd"
app.config['SECRET_KEY'] = SECRET_KEY

import part1





#index page greeting and Form Code
class MyForm(FlaskForm):
    """Contact/Location form."""
    username = StringField(
        'Username',
        [DataRequired()]
    )
    
    body = TextField(
        'Location',
        [
            DataRequired()
        ]
    )
    
    submit = SubmitField('Submit')



@app.route('/', methods = ['POST', 'GET'])
def hello():
    "this function is reading the html page to allow the user to fill out the form for a designated location"
    # return render_template ('hello.html')
    form = MyForm() 
    # if request.method == 'POST' and form.validate(): 
    #     data - request.form[""]  
    #     return redirect(url_for('/data')) 
    return render_template('signup.html', form=form) 



#backend
#POST submission
# os.system('python part1.py')

@app.route('/nearest_mbta')
def extract_data(location):
    ""





@app.route('/mbta_station', methods = ['POST', 'GET'])
#TODO: create a link between the data of Part1 to /mbta_station 
def data():
    """This function is presenting the data that was extracted from Part1"""
    if request.method == 'POST':
        f = open('part1.py')
        for line in f:
            print(line)
        # return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'GET':
    # if request.method == 'POST':
        # form_data = request.form
        print("it is a post ")

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


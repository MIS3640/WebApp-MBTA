# I am currently working on it, I am trying to figure out how to get the forms 
# to show. I just wanted to make sure you guys saw at least something of progress on this section.


from flask import Flask
import requests

# import part1
app = Flask(__name__)

#index page
@app.route('/')
def greeting(name=None):
    if name:
        return f"hello, {name}!"
    return "Hello, world!"

#form Code
#--in the works--
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class reusableform(Form):
    name = TextField('Name:', validators=[validators.required()])

    @app.route('/', methods=['GET', 'POST'])
    def location_form():
        form = reusableform(request.form)

        # print form.errors
        if request.method == 'POST':
            name = request.form['name']
            print (name)

        if form.validate():
            flash('Hello' + name)
        else:
            flash('All the form fields are required. ')
        return render_template('hello.html' , form=form)




# def post_request():
#     url = 
#     myobj = {'somekey': 'somevalue'}

#     x = request.ost(url, data = myobj)

if __name__ == "__main__":
    app.run(debug=True)

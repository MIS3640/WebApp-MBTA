# I am currently working on it, I am trying to figure out how to get the forms 
# to show. I just wanted to make sure you guys saw at least something of progress on this section.


from flask import Flask, render_template, request 



app = Flask(__name__)


#index page greeting
@app.route('/')
def greeting(name=None):
    if name:
        return f"hello, {name}!"
    return "Hello! Welcome to the site!"



#form Code
# --in the works--
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    Name= StringField('name', validators = [DataRequired()])

@app.route('/location', methods = ['POST'])
def location(): 
    form = LocationForm(request.form) 
    if request.method == 'POST' and form.validate(): 
        user = User(form.username.data, form.email.data) 
        db_session.add(user) 
        flash('The email address is'" +email+")
        return redirect(url_for('login')) 
    return render_template('location', form=form) 

@app.route('/form')
def location_form():
    return render_template('index.html')

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


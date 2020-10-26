from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nearest', methods=['GET', 'POST'])
def nearest():
    if request.method == 'POST':
        location = request.form
        return redirect(url_for("nearest_mbta", location = location))
    else:
        return render_template('mbta_html.html')

@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta(location):
    return location
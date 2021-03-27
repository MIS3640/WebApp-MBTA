from flask import Flask,request
from assignment3 import find_stop_near
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        place = request.form('place')
        nearest_stop = find_stop_near(place)
        if nearest_stop:
            return nearest_stop
    return 'fuck'


if __name__ == "__main__":
    app.run(debug=True)

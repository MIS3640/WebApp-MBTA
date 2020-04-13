"""
Simple "Hello, World" application using Flask
"""

from flask import Flask , render_template, request

from mbta_helper import find_stop_near


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)


@app.route("/nearest/", methods=["GET", "POST"])
def nearest():
    if request.method == "POST":
        place_name = str(request.form["place_name"])
        mbta_stop = find_stop_near(place_name)

        if mbta_stop:
            return render_template(
                "mbta_result.html", place_name=place_name , mbta_stop=mbta_stop
            )
        else:
            return render_template("mbta_form.html", error=True)
    return render_template("mbta_form.html", error=None)
    
if __name__=="__main__":
    app.run(debug=True)

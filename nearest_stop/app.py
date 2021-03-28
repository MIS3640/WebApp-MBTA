from flask import Flask, render_template, request
from assignment3 import find_stop_near
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def closest_stop():
    if request.method == "POST":
        place = str(request.form['place'])
        try:
            route_type = int(request.form['route_type'])
            nearest_stop = find_stop_near(place, route_type)
        except:
            nearest_stop = find_stop_near(place)
        if nearest_stop:
            return render_template('result.html', 
                nearest_stop=nearest_stop)
    else:
        return render_template('index.html')
    return render_template('index_html')


if __name__ == "__main__":
    app.run(debug=True)

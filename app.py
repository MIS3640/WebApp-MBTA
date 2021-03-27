from flask import Flask, render_template, redirect
from forms import GeoForm

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = GeoForm()
    if form.is_valid:
        return render_template('mbta.html')
    return render_template('index.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)

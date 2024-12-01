from flask import Flask, render_template
from wether_api import get_weather_info

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", info=get_weather_info(city="kiev"))


app.run()

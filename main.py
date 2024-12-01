from flask import Flask, render_template, request
from wether_api import get_weather_info_one, get_weather_json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    city = request.form.get("city")
    if not city:
        return render_template("index.html")
    json_api = get_weather_json(city=city)
    return render_template("index.html", info=get_weather_info_one(data=json_api))


@app.route(rule="/days")
def weather():
    ...


app.run()

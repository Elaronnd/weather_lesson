from flask import Flask, render_template, request
from weather_api import get_weather_info_one, get_weather_json, get_weather_info_multi

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    city = request.form.get("city")
    if not city:
        return render_template("index.html")
    json_api = get_weather_json(city=city)
    return render_template("index.html",
                           info=get_weather_info_one(data=json_api))


@app.route(rule="/days", methods=["GET", "POST"])
def weather():
    city = request.form.get("city")
    if not city:
        return render_template("days.html")
    json_api = get_weather_json(city=city, endpoint="forecast")
    return render_template("days.html",
                           multiinfo=get_weather_info_multi(data=json_api))


app.run()

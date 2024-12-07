import requests


def get_weather_json(city: str, endpoint: str = "weather"):
    appid = "fb696f74063ae07dd7b08103d1f8b4d0"
    result = requests.get(
        f"https://api.openweathermap.org/data/2.5/{endpoint}?q={city}&lang=ua&units=metric&appid={appid}"
    )
    if result.status_code != 200:
        return {}
    return result.json()


def get_weather_info_one(data):
    main_weather = data.get("weather")[0].get("main")

    main = data.get("main")

    main_temp = main.get("temp")

    main_fells_like = main.get("feels_like")

    name = data.get("name")

    visibility = data.get("visibility")

    wind = data.get("wind")

    wind_speed = wind.get("speed")

    wind_deg = wind.get("deg")

    clouds = data.get("clouds")

    clouds_all = clouds.get("all")
    json_weather = {
        "weather": main_weather,
        "temp": f"{main_temp} °C",
        "fells_like": f"{main_fells_like} °C",
        "city": name,
        "visibility": f"{visibility} м.",
        "wind_speed": f"{wind_speed} м/с",
        "wind_deg": f"{wind_deg}°",
        "clouds_all": f"{clouds_all}%"
    }
    return json_weather


def get_weather_info_multi(data, days: int = 5):
    data = data.get("list")
    result = []
    date_weather = ""
    if data is None:
        return []
    for weather in data:
        dt_txt = weather.get("dt_txt")[0:10]
        if len(result) == days:
            break
        elif date_weather != dt_txt:
            info = get_weather_info_one(weather)
            info["date_weather"] = dt_txt
            result.append(info)
            date_weather = dt_txt
    return result

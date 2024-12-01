import requests


def get_weather_info(city: str):
    appid = "key"
    result = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ua&units=metric&appid={appid}"
    )
    if result.status_code != 200:
        return {}
    main_weather = result.json().get("weather")[0].get("main")

    main = result.json().get("main")

    main_temp = main.get("temp")

    main_fells_like = main.get("feels_like")

    name = result.json().get("name")

    visibility = result.json().get("visibility")

    wind = result.json().get("wind")

    wind_speed = wind.get("speed")

    wind_deg = wind.get("deg")

    clouds = result.json().get("clouds")

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

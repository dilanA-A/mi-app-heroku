from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = "e4b8dfac9272382dd271647ef0b735b0"  # ⚠️ Reemplaza con tu API key de OpenWeather

@app.route("/", methods=["GET", "POST"])
def clima():
    clima_data = None
    if request.method == "POST":
        ciudad = request.form["ciudad"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            clima_data = {
                "ciudad": ciudad.title(),
                "temperatura": data["main"]["temp"],
                "descripcion": data["weather"][0]["description"],
                "icono": data["weather"][0]["icon"],
            }
        else:
            clima_data = {"error": "Ciudad no encontrada"}
    return render_template("index.html", clima=clima_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

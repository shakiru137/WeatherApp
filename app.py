from flask import Flask, render_template, request
import requests
app = Flask(__name__)

API_KEY = "680b02b7d5e2052b5a3f159fe7430f80"

@app.route("/", methods=["GET", "POST"])
def get_weather():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                weather = response.json()
            else:
                error = f"City '{city}' not found. Please check spelling or try another nearby city."

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5500)
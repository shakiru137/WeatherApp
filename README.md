# 🌦️ Weather App with Flask

A simple and elegant weather application built with **Flask** that lets users search for current weather conditions in any city worldwide using the **OpenWeatherMap API**.

---

## 🚀 Features

- 🌍 Get real-time weather by city name
- ❌ Error handling with suggestions for misspelled or invalid cities
- 🌡️ Displays temperature, humidity, pressure, visibility, wind, and more
- 📱 Mobile-friendly modern UI (requires CSS file)
- 🔁 Built with Flask and Jinja2 templating

---

## 🛠️ Technologies Used

- Python 3
- Flask
- HTML + Jinja2 Templates
- OpenWeatherMap API
- (Optional) LocalTunnel or similar for public access

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/weatherApp.git
cd weatherApp
```

python -m venv venv
source venv/bin/activate # On Linux/macOS
venv\Scripts\activate # On Windows

pip install flask requests

python3 app.py

To make your app accessible online temporarily, use tools like:
npx localtunnel --port 5500

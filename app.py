import streamlit as st
import requests
import os

# ✅ Get your API key securely (set this in Streamlit Secrets)
API_KEY = st.secrets.get("OPENWEATHER_API_KEY") or os.getenv("OPENWEATHER_API_KEY")

# 🌤 Function to fetch weather data
def get_weather(city):
    if not API_KEY:
        return "❌ API key not set. Please add OPENWEATHER_API_KEY in Streamlit Secrets."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return "⚠️ City not found. Try again."

    data = response.json()
    weather = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    result = (
        f"🌍 **City:** {city}\n"
        f"🌤 **Weather:** {weather}\n"
        f"🌡 **Temperature:** {temp}°C (Feels like {feels_like}°C)\n"
        f"💧 **Humidity:** {humidity}%"
    )
    return result


# 🚀 Streamlit App UI
st.set_page_config(page_title="Weather App", page_icon="☀️", layout="centered")

st.title("☀️ Weather App")
st.write("Enter a city name below to get current weather conditions:")

city = st.text_input("City", placeholder="e.g. Islamabad")

if st.button("Get Weather"):
    if city:
        report = get_weather(city)
        st.markdown(report)
    else:
        st.warning("Please enter a city name.")

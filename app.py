import gradio as gr
import requests
import os

# Get your API key from https://openweathermap.org/api
API_KEY = os.getenv("OPENWEATHER_API_KEY")  # set as secret on Hugging Face

def get_weather(city):
    if not API_KEY:
        return "❌ API key not set. Please add OPENWEATHER_API_KEY in Hugging Face Secrets."
    
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
        f"🌍 City: {city}\n"
        f"🌤 Weather: {weather}\n"
        f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)\n"
        f"💧 Humidity: {humidity}%"
    )
    return result


with gr.Blocks() as demo:
    gr.Markdown("# ☀️ Weather App")
    gr.Markdown("Enter a city name to get current weather conditions.")

    city = gr.Textbox(label="City", placeholder="e.g. Islamabad")
    output = gr.Textbox(label="Weather Report")
    btn = gr.Button("Get Weather")

    btn.click(get_weather, inputs=city, outputs=output)

if __name__ == "__main__":
    demo.launch()

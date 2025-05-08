import requests
import os # allows us to manipulate files, find files
from dotenv import load_dotenv #openAI client

# gets path of current file + combines with: \.env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

# execute the current python process
load_dotenv(dotenv_path=dotenv_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error while making request: ", e)
        return None

def display_weather(data):
    if data:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
    else:
        print("No data to display.")



if __name__ == "__main__":
    city = input("Enter a city name: ")
    data = get_weather(city)
    display_weather(data)
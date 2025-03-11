import requests

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(location):
    """
    Fetch weather data for the specified location (city or ZIP code).
    """
    params = {
        "q": location,  # Location (city name or ZIP code)
        "appid": API_KEY,  # API key
        "units": "metric"  # Use metric units (Celsius)
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(data):
    """
    Display weather information to the user.
    """
    if data is None:
        print("No weather data available.")
        return

    # Extract relevant data
    city = data.get("name", "Unknown Location")
    weather = data.get("weather", [{}])[0].get("description", "Unknown")
    temperature = data.get("main", {}).get("temp", "Unknown")
    humidity = data.get("main", {}).get("humidity", "Unknown")

    # Display the weather information
    print(f"\nWeather in {city}:")
    print(f"Conditions: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")

def main():
    # Prompt the user for a location
    location = input("Enter a city name or ZIP code: ")

    # Fetch weather data
    weather_data = get_weather_data(location)

    # Display the weather data
    display_weather(weather_data)

# Run the program
if __name__ == "__main__":
    main()
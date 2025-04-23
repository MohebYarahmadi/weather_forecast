import requests

API_KEY = "4fe5208a9b83a94d04d7f9ee1a29c2a7"
PI = "141710af2113bab9f55ef73e1bcd33d5"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={PI}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    try:
        print(get_data("Tokyo", forecast_days=3))
    except:
        print("City not found.")

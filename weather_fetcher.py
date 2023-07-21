import requests

API_KEY = 'd0ad4d7ebaa8dd38e97424a5b856a3ac'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city_name = input('Enter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city_name}'

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = (data['main']['temp'] - 273.15) * (9/5) + 32

    print(f'The weather today is {weather}')
    print(f'The temperature is {temperature:.2f}')
else:
    print('An error occured.')
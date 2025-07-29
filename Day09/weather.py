import requests 
city = input('City:')
key = '39be8355f4c2b070862ba7ea33d969fa'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
response = requests.get(url)
if response.status_code == 200:
    weatherJson = response.json()
    #print(weatherJson)
    print(f'City:{weatherJson["name"]}')
    print(f'Temperature:{weatherJson["main"]["temp"]}K')
    print(f'Description:{weatherJson["weather"][0]["description"]}')
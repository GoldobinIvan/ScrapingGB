import requests
import json

url = 'http://api.weatherapi.com/v1/current.json?key=93d88a3481c54b6a8ed144544222104&q=Moscow&aqi=no'
req = requests.post(url)
print(req.status_code)

with open('weatherapi.json', 'w') as outfile:
    json.dump(req.json(), outfile)
import requests
import json

response=requests.get("https://openweathermap.org/api")
print(response.json())
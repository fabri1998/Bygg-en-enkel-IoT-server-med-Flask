import requests

url = 'http://127.0.0.1:5000/sensor'
data = {"temperature": 22.5, "humidity": 60, "illuminance": 15.0, "activepower": 0.9}
response = requests.post(url, json=data)
print(response.json())
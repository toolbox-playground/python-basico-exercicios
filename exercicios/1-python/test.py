import requests

response = requests.get("https://google.com")
print('Hello world!', response.status_code)
import requests

url = "https://api.github.com/users"

response = requests.get(url)

data = response.json()

for user in data:
    print(user["login"])
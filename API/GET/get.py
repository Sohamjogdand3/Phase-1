import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

data = response.json()

username = data["login"]
user_id = data["id"]

print("Username:", username)
print("ID:", user_id)
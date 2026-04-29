import requests

url = "https://restcountries.com/v3.1/name/india"

response = requests.get(url)

data = response.json()

country = data[0]

print("Country:", country["name"]["common"])
print("Capital:", country["capital"][0])
print("Population:", country["population"])
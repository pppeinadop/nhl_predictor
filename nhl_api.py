import requests

url = "https://api-web.nhle.com/v1/standings/now"

response = requests.get(url)

data = response.json()

print("\nEQUIPOS NHL\n")

for team in data["standings"]:
    print(team["teamName"]["default"])
import requests

url = "https://icanhazdadjoke.com/"

res = requests.get(url, headers={"Accept": "application/json"})

# print(type(res.text))
# print(type(res.json()))

data = res.json()
print(data["joke"])
print(f"status: {data['status']}")

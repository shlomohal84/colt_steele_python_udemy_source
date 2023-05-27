import requests

url = "http://www.google.com/fqfqfqfqwqwdd/fqefqfq"
res = requests.get(url)

print(f"Your request to {url} came back with status code {res.status_code}")

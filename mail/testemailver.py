import requests

url = "https://api.reacher.email/v0/check_email"
payload = {"to_email":"amaury@reacher.email"}
response = requests.post(url, json=payload)

print(response.text)
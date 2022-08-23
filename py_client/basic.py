import requests


endpoint = "http://localhost:8000/api/v1/"
get_response = requests.post(endpoint, json={"title": "Hello", "discount": "AA"})

print()
print(type(get_response.json()))
print(get_response.json())
print()

import requests


endpoint = "http://localhost:8000/api/"
get_response = requests.post(endpoint, params={'query': 'AABB'}, json={"title": "Hello WoRld"})

print('text -> ', type(get_response.text))
print(get_response.text)
print()
print('json -> ', type(get_response.json()))
print(get_response.json())
print()

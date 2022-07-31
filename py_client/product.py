import requests


endpoint = 'http://localhost:8000/api/products/9/update/'
data = {
  'title': 'Hello World 4'  
}

get_response = requests.delete(endpoint)

print('text -> ', type(get_response.text), get_response.status_code)
print(get_response.text)
print()
print('json -> ', type(get_response.json()), get_response.status_code)
print(get_response.json())
print()

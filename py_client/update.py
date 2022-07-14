import requests


endpoint = "http://localhost:8000/api/products/5/update/"

data = {
  'title': 'Title updated',
  'price': 150.5
}
get_response = requests.put(endpoint, json=data)
print('-->', get_response.json())

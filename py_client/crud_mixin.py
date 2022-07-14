import requests


endpoint = "http://localhost:8000/api/products/6/mixin/"

data = {
  'title': 'Test Mixin Title Update',
  'price': 763.99
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())

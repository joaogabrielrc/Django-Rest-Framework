import requests


endpoint = "http://localhost:8000/api/products/9/delete/"

get_response = requests.delete(endpoint)

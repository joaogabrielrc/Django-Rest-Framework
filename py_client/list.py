import requests
from getpass import getpass


auth_endpoint = 'http://localhost:8000/api/auth/'

username = input('What is your username? ')
password = getpass('What is your password? ')
credentials = {
  'username': username,
  'password': password
}

auth_response = requests.post(auth_endpoint, json=credentials)

if auth_response.status_code == 200:
  token = auth_response.json()['token']
  headers = {
    'Content-Type': 'application/json',   
    'Authorization': f'Bearer {token}'
  }

  endpoint = 'http://localhost:8000/api/products/'

  get_response = requests.get(endpoint, headers=headers)
  print(get_response.json())

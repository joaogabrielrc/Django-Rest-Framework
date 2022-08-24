from email import header
import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/v1/auth/"
username = input("Username: ")
password = getpass()

auth_response = requests.post(auth_endpoint, json={"username": username, "password": password})

if auth_response.status_code == 200:
  token = auth_response.json().get("token")
  headers = {
    "Authorization": f"Bearer {token}"
  }
  endpoint = "http://localhost:8000/api/v1/products/1"

  get_response = requests.get(endpoint, headers=headers)

  print()
  print(type(get_response.text))
  print(get_response.text)
  print()

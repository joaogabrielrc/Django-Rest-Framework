from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


User = get_user_model()

class UserPermissionsTestCase(TestCase):      
  def test_admin_has_permission(self):
    manager_a = User.objects.create_user(
      username="user_a", 
      password="pass123",
      is_staff=True
    )   
    token = Token.objects.get_or_create(user=manager_a)[0]    
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    endpoint = "/api/v1/products/"
    response = client.get(endpoint)    
    self.assertEqual(response.status_code, 200)  


  def test_employee_has_permission(self):
    employee_a = User.objects.create_user(
      username="employee_a", 
      password="pass123"
    )
    token = Token.objects.get_or_create(user=employee_a)[0]    
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    endpoint = "/api/v1/products/"
    response = client.get(endpoint)    
    self.assertEqual(response.status_code, 403)  

from django.db import models


class Product(models.Model):
  title = models.CharField(max_length=120)
  content = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
  is_active = models.BooleanField(default=True)

  def __str__(self) -> str:
    return self.title

  def get_discount(self) -> float:
    return 0.8

  @property
  def sale_price(self) -> float:
    price = float(self.price)
    discount = self.get_discount()     
    return f'{price * discount:.2f}'



from django.db import models

class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=200)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.supplier_name

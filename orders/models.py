from django.db import models
from suppliers.models import Suppliers

class Orders(models.Model):
    supplier_id = models.ForeignKey(Suppliers, max_length=200,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=200)
    total_amount=models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.order_date
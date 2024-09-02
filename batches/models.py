from django.db import models
from medicine.models import Medicine

class batches(models.Model):
    # batch_name = models.CharField(max_length=200)
    medicine_id = models.ForeignKey(Medicine,max_length=50, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=50)
    manufacturing_date = models.CharField(max_length = 50)
    expiry_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.batch_name
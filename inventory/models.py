from django.db import models
from medicine.models import Medicine
from batches.models import batches
class Inventory(models.Model):
    medicine_id = models.ForeignKey(Medicine, max_length=200,on_delete=models.CASCADE)
    batch_id = models.ForeignKey(batches, max_length=200,on_delete=models.CASCADE)
    current_stock = models.IntegerField()
    reorder_level = models.IntegerField()
    storage_location=models.CharField(max_length=200)
    last_updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.batch_name
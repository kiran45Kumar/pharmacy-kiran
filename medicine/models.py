from django.db import models
import PIL

class Medicine(models.Model):
    generic_name = models.CharField(max_length=50)
    med_image = models.ImageField(default="",upload_to='uploads/')
    brand_name = models.CharField(max_length=50)
    category = models.CharField(max_length = 50)
    dosage_form = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.CharField(max_length=50)
    composition = models.CharField(max_length=50)
    indications = models.CharField(max_length=50)
    contraindications = models.CharField(max_length=50)
    side_effects = models.CharField(max_length=50)
    barcode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return self.generic_name
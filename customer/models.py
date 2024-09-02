from django.db import models

class Customer(models.Model):
    email = models.CharField(max_length=50)  
    password = models.CharField(max_length=60, null=False, blank=False)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    role = models.CharField(max_length=100, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name

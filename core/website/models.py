from django.db import models
from accounts.validators import validate_iranian_cellphone_number

class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    message=models.TextField()
    phone_number = models.CharField(max_length=12, validators=[validate_iranian_cellphone_number])
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_date']
    
    def __str__(self):
        return self.name
    
class Newsletter(models.Model):
    email=models.EmailField()
    
    def __str__(self):
        return self.email
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#company model


class company_detail(models.Model):
    seller_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    seller_address = models.TextField(max_length=400)
    

    def __str__(self):
        return self.seller_name

#product model
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.FloatField()
    product_quantity= models.SmallIntegerField()

    def __str__(self):
        return self.product_name

#invoice model
class invoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    mobile_no = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    company_name = models.ForeignKey(company_detail, on_delete=models.PROTECT, default='')
    product_name = models.ManyToManyField(Product, default='')
    


    def __str__(self):
        return self.customer_name
    
class UserProfile(AbstractUser):
    invoice_field = models.ManyToManyField(invoice)


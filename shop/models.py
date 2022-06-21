from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    sub_category= models.CharField(max_length=50)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")
    

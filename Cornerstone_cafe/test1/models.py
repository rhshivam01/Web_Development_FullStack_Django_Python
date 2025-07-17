from django.db import models
import datetime
# Create your models here.
class Products(models.Model):
    product_id = models.CharField(max_length = 100 , unique=True)
    product_name = models.CharField(max_length = 100)
    product_description = models.CharField(max_length = 400)
    product_category = models.CharField(max_length = 100)
    product_img = models.ImageField(upload_to='Images/', default=None, blank=True, null=True)

    def __str__(self):
        return self.product_id
    
class contact_query(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField(max_length=15)
    date = models.DateTimeField(("Date"), default = datetime.datetime.today)

    def __str__(self):
        return self.email

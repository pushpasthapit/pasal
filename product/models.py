from django.db import models

# Create your models here.
class Product(models.Model):
	Product_type = models.CharField(max_length = 100)
	Product_name = models.CharField(max_length = 100)
	Product_code = models.CharField(max_length = 100)
	price = models.IntegerField()
	created_date = models.TimeField(auto_now = True)
	updated_date = models.TimeField(auto_now = True)




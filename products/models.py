from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Discount(models.Model):
	coupon = models.CharField(max_length=5)
	off = models.FloatField(default=0.0)
	purpose = models.CharField(max_length=255)
	
	def __str__(self):
		return self.purpose +' -> ' + str(self.off) + ' %'

class Product(models.Model):
	name = models.CharField(max_length=255)
	img_url = models.CharField(max_length=2083)
	stock = models.IntegerField(default=0)
	price = models.FloatField(default=0.0)
	discription = models.TextField()
	import_date = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	discount = models.ForeignKey(Discount, on_delete=models.CASCADE, default=True)
	def __str__(self):
		return self.name 


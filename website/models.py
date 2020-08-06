from django.db import models


# Create your models here.
class Item(models.Model):
	item = models.CharField(max_length=100)
	price = models.FloatField()
	category = models.CharField(max_length=2)
	label = models.CharField(max_length=1)
	description = models.TextField()
	image = models.ImageField()
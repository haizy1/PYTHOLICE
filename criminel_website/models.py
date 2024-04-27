from django.db import models


class Users(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	email = models.EmailField('Email User')
	def __str__(self):
		return self.first_name +' '+ self.last_name

# Create your models here.

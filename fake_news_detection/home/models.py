from django.db import models

# Create your models here.
class Facts(models.Model):
    fact = models.TextField(default='Enter your facts here....')
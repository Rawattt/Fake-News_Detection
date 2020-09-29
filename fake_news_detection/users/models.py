from django.db import models

# Create your models here.
class FakeNews(models.Model):
    news = models.TextField(default = 'Enter your facts here....')
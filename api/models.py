from django.db import models

# Create your models here.


class Log(models.Model):
    telegramId = models.CharField(max_length=15)
    url = models.CharField(max_length=255)
    request = models.TextField()
    response = models.TextField()

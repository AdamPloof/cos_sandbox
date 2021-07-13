from django.db import models

class Profile(models.Model):
    style = models.CharField(max_length=50)

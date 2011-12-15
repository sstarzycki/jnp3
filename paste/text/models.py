from django.db import models
from django.contrib.auth.models import User

class Text(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField(max_length=255)
    description = models.CharField(max_length=255)
    upload_date = models.DateTimeField()
# Create your models here.

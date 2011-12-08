from django.db import models
from django.contrib.auth.models import User

class Text(models.Model):
    user = models.OneToOneField(User)
    content = models.TextField()
    description = models.CharField(max_length=256)
# Create your models here.

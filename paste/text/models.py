from django.db import models
from django.contrib.auth.models import User
import datetime

class Text(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField(max_length=255)
    description = models.CharField(max_length=255)
    upload_date = models.DateTimeField(null=True)
    update_date = models.DateTimeField(null=True)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.upload_date = datetime.datetime.today()
        self.update_date = datetime.datetime.today()
        super(Text, self).save(*args, **kwargs)

# Create your models here.

from django.db import models
import datetime
import mongoengine

class Text(mongoengine.Document):
    content = mongoengine.StringField()
    title = mongoengine.StringField()
    upload_date = mongoengine.DateTimeField(required=False)
    update_date = mongoengine.DateTimeField(required=False)
    user_id = mongoengine.IntField(required=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.upload_date = datetime.datetime.today()
        self.update_date = datetime.datetime.today()
        super(Text, self).save(*args, **kwargs)

# Create your models here.

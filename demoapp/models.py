from django.db import models
import datetime

class Post(models.Model):
        comment = models.CharField(max_length=250)
        created = models.DateField(default = datetime.date.today)

        def __str__(self):
            return self.comment

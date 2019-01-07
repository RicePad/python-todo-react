from django.db import models

# Create your models here.

class ToDo(models.Model):
        title =  models.CharField(max_length=50)
        description = models.TextField(max_length=200)
        completed = models.BooleanField(default=False)


        def _str_(self):
            return self.title

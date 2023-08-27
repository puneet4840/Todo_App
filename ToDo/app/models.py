from django.db import models
from datetime import datetime 
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
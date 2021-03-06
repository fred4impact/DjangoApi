from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Event(models. Model):
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    url = models.URLField(default="www")
    timestamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
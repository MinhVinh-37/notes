from django.db import models
from accounts.models import User

class Note(models.Model):
    title = models.CharField()
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

from django.db import models
from accounts.models import User


class Note(models.Model):
    class Meta:
        verbose_name = "note"
        db_table = "note"
        
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

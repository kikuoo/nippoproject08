from django.db import models

class NippoModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    

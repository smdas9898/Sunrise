from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title

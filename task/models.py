from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=256)
    due_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True, auto_now=True)

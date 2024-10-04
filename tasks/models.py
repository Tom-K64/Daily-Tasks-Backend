from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20,null=True, blank=True)
    status = models.CharField(max_length=20,null=True, blank=True)
    order = models.PositiveIntegerField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

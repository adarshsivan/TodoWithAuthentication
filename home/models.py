from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    task_name = models.CharField(max_length=100)
    description = models.CharField(max_length= 300)
    created_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
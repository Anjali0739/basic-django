from django.db import models

# Create your models here.
class Task(models.Model):  # 👈 Creating a table named "Task"
    title = models.CharField(max_length=100)  # Text field (max 100 chars)
    created = models.DateTimeField(auto_now_add=True)  # Timestamp, set when created

    def __str__(self):
        return self.title  # How this model appears in admin/site output

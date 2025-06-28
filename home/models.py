from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):  # 👈 Creating a table named "Task"
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 👈 Link to user
    title = models.CharField(max_length=100)  # Text field (max 100 chars)
    created = models.DateTimeField(auto_now_add=True)  # Timestamp, set when created
    completed = models.BooleanField(default=False)  # ✅ NEW

    def __str__(self):
        return self.title  # How this model appears in admin/site output

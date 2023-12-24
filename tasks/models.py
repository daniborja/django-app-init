from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Task(models.Model): # inheritance: (models.Model)
    title = models.CharField(max_length=200)
    description = models.TextField()  # > charfield
    done = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    created_at = models.DateTimeField(
      auto_now_add=True # createdAt x default
    )
    completed_at = models.DateTimeField(null=True)

    # ### relations/associations (User 1:N Tasks) - User created by django x default
    user = models.ForeignKey(User, on_delete=models.CASCADE) # onDelete Cascade


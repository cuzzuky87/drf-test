from django.db import models
from django.contrib.auth.models import User
import uuid

class Todo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=150)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
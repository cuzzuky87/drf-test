from django.db import models
import uuid

class Todo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
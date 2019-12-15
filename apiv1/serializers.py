from rest_framework import serializers
from todo import models

class TodoSerializer(serializers.Serializer):
    class Meta:
        fields = (
            'pk',
            'title',
            'description'
        )
        model = models.Todo
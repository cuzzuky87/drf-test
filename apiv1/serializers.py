from rest_framework import serializers
from todo import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'user'
        )
        model = models.Todo
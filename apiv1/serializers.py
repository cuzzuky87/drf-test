from rest_framework import serializers
from todo import models

class TodoSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    description = serializers.CharField()
    class Meta:
        fields = (
            'id',
            'title',
            'description'
        )
        model = models.Todo
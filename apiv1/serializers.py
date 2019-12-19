from rest_framework import serializers
from django.contrib.auth.models import User
from todo import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","last_login",)
        read_only_fields = ('last_login',)
    
class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'user'
        )
        model = models.Todo

from rest_framework import serializers
from django.contrib.auth.models import User
from todo import models
from testapp.models import Task

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


class TestappSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'created_at',
            'modified_at',
            'user'
        )
        model = Task
from rest_framework import serializers
from django.contrib.auth.models import User
from todo import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","last_login",)
        read_only_fields = ('last_login',)
        extra_kwargs = {"id":{'read_only':False}}
    
    
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

    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.get(pk=user_data["id"])
        todo = models.Todo.objects.create(user=user,**validated_data)
        return todo 

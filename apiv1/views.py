from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from rest_framework import viewsets
from rest_framework.response import Response

from todo.models import Todo
from .serializers import TodoSerializer, TestappSerializer

from testapp.models import Task



class ListTodo(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TestappViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Task.objects.all()
        serializer = TestappSerializer(queryset, many=True) 
        return Response(serializer.data)
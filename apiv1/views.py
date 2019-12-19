from rest_framework.generics import ListCreateAPIView,RetrieveAPIView

from todo.models import Todo
from .serializers import TodoSerializer


class ListTodo(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

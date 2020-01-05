from django.urls import path,include

from rest_framework.routers import DefaultRouter


from .views import ListTodo,DetailTodo, TestappViewSet

router = DefaultRouter()
router.register(r'testapp', TestappViewSet, basename='testapp')


urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/',DetailTodo.as_view()),
    path('test/', include(router.urls))
    
]
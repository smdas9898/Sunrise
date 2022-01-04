from django.urls import path
from .views import CreateTask

app_name = "task"

urlpatterns = [
    path('create/', CreateTask.as_view(), name='create-task'),
    path('list_task/', CreateTask.as_view(), name='list-task'),
]

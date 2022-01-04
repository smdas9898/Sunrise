from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response

class TaskService():
    def create(self, data):
        try:
            task_object = Task.objects.create(title=data['title'], details=data['details'])
            return task_object
        except Exception:
            return "Error in query params"

    def create_using_serializer(self, data):
        serializer = TaskSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return serializer
           
    def get_all(self):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return serializer.data

from rest_framework.views import APIView
from .services import TaskService
from .models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import serializers, status


class CreateTask(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, format=None):
        """
        Return a list of all users.
        """
        tasks = TaskService().get_all()
        return Response(tasks)
    
    def post(self, request, format=None):
        task_create = TaskService().create(request.data)

        # task_create = TaskService().create_using_serializer(request.data)
        if task_create: 
            return Response({'msg': 'Task Created'}, status=status.HTTP_201_CREATED)
        
        return Response(task_create.errors, status=status.HTTP_400_BAD_REQUEST)

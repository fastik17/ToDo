from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from task.api.v1.serializers import TaskSerializers
from task.models import Task


class TaskViewSet(ModelViewSet):
    """All list of tasks"""

    serializer_class = TaskSerializers
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
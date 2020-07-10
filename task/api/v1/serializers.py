from rest_framework import serializers

from task.models import Task


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'text', 'due_date', 'created']
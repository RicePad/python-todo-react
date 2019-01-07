from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo.objects.all()
        fields = ('id', 'title', 'description', 'completed')
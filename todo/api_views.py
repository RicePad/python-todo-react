from django.shortcuts import render
from rest_framework import viewsets
from todo.serializers import ToDoSerializer
from todo.models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

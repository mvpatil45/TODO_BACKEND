from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer

class TodoDetailView(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer
    
class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer
    
class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

# A viewset that automatically provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

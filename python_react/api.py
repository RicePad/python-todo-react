from rest_framework import routers
from todo import api_views

router = routers.DefaultRouter()
router.register(r'todo', api_views.ToDoViewSet)

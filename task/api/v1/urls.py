from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task.api.v1.viewsets import TaskViewSet


router = DefaultRouter()
router.register('task', TaskViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
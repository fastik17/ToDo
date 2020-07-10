from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .viewsets import SignupViewSet


router = DefaultRouter()
router.register('signup', SignupViewSet, basename='signup')


urlpatterns = [
    path("", include(router.urls)),
]
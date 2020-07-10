from rest_framework.viewsets import ModelViewSet
from users.api.v1.serializers import SignupSerializer


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ['post']
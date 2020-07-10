from rest_framework import serializers

from users.models import User


class SignupSerializer(serializers.ModelSerializer):
    """Serializer for creating user objects."""

    class Meta:
        model = User
        fields = ('id', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

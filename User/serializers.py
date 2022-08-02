from rest_framework import serializers

from User.models import CustomUser


class UsersSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователей """
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'is_active', 'is_staff', 'date_joined']


class CreateUserSerializer(serializers.ModelSerializer):
    """"Создаем пользователя"""
    password = serializers.CharField(max_length=128,
                                     min_length=8,
                                     write_only=True,
                                     )

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', ]
        read_only_fields = ('id',)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    """
    Authenticates an existing user.
    Email and password are required.
    Returns a JSON web token.
    """
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)



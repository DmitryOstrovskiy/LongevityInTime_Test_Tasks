from django.core.validators import MinLengthValidator, MaxLengthValidator

from djoser.serializers import UserCreateSerializer as UserCreate
from djoser.serializers import UserSerializer

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User
from api.validators import (validate_username, validate_password,
                            validate_first_name, validate_last_name)

MAX_LENGTH_EMAIL = 254
MAX_LENGTH_USERNAME = 50
MIN_LENGTH_PASSWORD = 6
MAX_LENGTH_PASSWORD = 15


class UserCreateSerializer(UserCreate):
    username = serializers.CharField(
        validators=[UniqueValidator(
                message='This username is already taken',
                queryset=User.objects.all()),
            validate_username],
        required=True)
    email = serializers.EmailField(
        validators=[UniqueValidator(
                message='This email is already taken',
                queryset=User.objects.all()),
            MaxLengthValidator(
                limit_value=MAX_LENGTH_EMAIL,
                message=(
                    'Email must be shorter than'
                    f'{MAX_LENGTH_EMAIL} characters'))],
        required=True)
    first_name = serializers.CharField(
        max_length=MAX_LENGTH_USERNAME,
        help_text='Enter your first name',
        validators=[validate_first_name],
        required=True)
    last_name = serializers.CharField(
        max_length=MAX_LENGTH_USERNAME,
        help_text='Enter your last name',
        validators=[validate_last_name],
        required=True)
    password = serializers.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        required=True,
        write_only=True,
        validators=[
            MinLengthValidator(
                limit_value=MIN_LENGTH_PASSWORD,
                message='The password must be more than f{MIN_LENGTH_PASSWORD} characters'
            ),
            MaxLengthValidator(
                limit_value=MAX_LENGTH_PASSWORD,
                message='The password must be less than f{MAX_LENGTH_PASSWORD} characters'
            ),
            validate_password],
        help_text=(
            'The password must contain lowercase and uppercase letters and numbers'),)

    class Meta(UserCreate.Meta):
        model = User
        fields = (
            'id', 'email', 'first_name',
            'last_name', 'username', 'password'
        )


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'first_name',
            'last_name', 'username'
        )

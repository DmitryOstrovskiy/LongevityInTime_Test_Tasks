from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


from .validators import validate_password, validate_username

MAX_LENGTH_EMAIL = 254
MAX_LENGTH_USERNAME = 50
MIN_LENGTH_PASSWORD = 6
MAX_LENGTH_PASSWORD = 15


class User(AbstractUser):
    """ Custom UserModel."""
    username = models.CharField(
        verbose_name='Username',
        validators=[validate_username],
        max_length=MAX_LENGTH_USERNAME,
        help_text='Enter the username',
        unique=True,
        db_index=True,
        blank=False
    )
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=MAX_LENGTH_EMAIL,
        help_text='Enter the email',
        blank=False,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=MAX_LENGTH_USERNAME,
        help_text='Enter your first name',
        blank=False
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=MAX_LENGTH_USERNAME,
        help_text='Type your last name',
        blank=False,
    )
    password = models.TextField(
        verbose_name='Password',
        max_length=MAX_LENGTH_USERNAME,
        blank=False,
        validators=[
            MinLengthValidator(
                limit_value=MIN_LENGTH_PASSWORD,
                message='The password must be more than 6 characters'
            ),
            MaxLengthValidator(
                limit_value=MAX_LENGTH_PASSWORD,
                message='The password must be less than 15 characters'
            ),
            validate_password
        ],
        help_text=(
            'The password must contain lowercase and uppercase letters and numbers'),
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'password']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

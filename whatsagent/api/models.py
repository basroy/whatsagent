
# Create your models here.
import uuid

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.


class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)


class ProjectModel(TimestampedModel):
    class Meta:
        abstract = True

    uid = models.UUIDField(unique=True, null=False, default=uuid.uuid4)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, ProjectModel):
    email = models.EmailField(
        verbose_name= 'Email address',
        max_length=255,
        unique=True
    )
    # is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
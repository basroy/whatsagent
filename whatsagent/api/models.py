
import uuid

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from whatsagent.api import models as mdl


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

    def create_user(self, name, terms, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        print(f'First argumant {name}')
        print(f'Second argumant {terms}')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            terms=terms
      )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # def _create_user(self, email, password=None, **other_required_fields):
    #     if not email:
    #         raise ValueError('Users must have an email address')
    #
    #     user = self.model(
    #         email=self.normalize_email(email),
    #         **other_required_fields
    #     )
    #
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_user(self, email, password=None, **other_required_fields):
    #     other_required_fields.setdefault("terms", False)
    #     other_required_fields.setdefault("name", False)
    #     return self._create_user(email,password,**other_required_fields)


class User(AbstractBaseUser, ProjectModel):
    email = models.EmailField(
        verbose_name= 'Email address',
        max_length=255,
        unique=True
    )
    name = models.CharField(
        max_length=255,
        unique=False
    )
    terms = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    # user: models.User = models.User.objects.create_user()
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class OrganizationManager(BaseUserManager):
    def create_organization(self, nameorganization, email, password=None):
        if not email:
            raise ValueError('У организации должен быть email')
        organization = self.model(
            nameorganization=nameorganization,
            email=self.normalize_email(email),
        )
        organization.set_password(password)
        organization.save(using=self._db)
        return organization


class Organization(AbstractBaseUser):
    nameorganization = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    objects = OrganizationManager()

    USERNAME_FIELD = 'nameorganization'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.nameorganization



from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

GENDER = [
    ("female", "Femenino"),
    ("male", "Masculino"),
    ("other", "Otro"),
]

class UserManager(BaseUserManager):
    def create_user(self, email, name, paternal_name, maternal_name, age, gender, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            paternal_name=paternal_name,
            maternal_name=maternal_name,
            age=age,
            gender=gender,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, paternal_name, maternal_name, age, gender, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, name, paternal_name, maternal_name, age, gender, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name            = models.CharField(max_length=100)
    paternal_name   = models.CharField(max_length=100)
    maternal_name   = models.CharField(max_length=100, blank=True, null=True, default="")
    age             = models.IntegerField()
    email           = models.EmailField(unique=True)
    gender          = models.CharField(max_length=10, choices=GENDER)
    phone           = models.CharField(max_length=20, blank=True, null=True)

    created_at      = models.DateTimeField(default=timezone.now)
    updated_at      = models.DateTimeField(auto_now=True)

    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)

    objects         = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "paternal_name", "maternal_name", "age", "gender"]

    def __str__(self):
        return self.email

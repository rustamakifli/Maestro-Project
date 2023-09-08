from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin,UserManager)
from core.utils import tools
from django.utils import timezone
from django.conf import settings

# Create your models here.
USER_MODEL = settings.AUTH_USER_MODEL

GENDER = (
    ("male", "Kişi"),
    ("female", "Qadın"),
)

class MyUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
    
class MyUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(("first name"), max_length=255, blank=True)
    last_name = models.CharField(("last name"), max_length=255, blank=True)
    birth_date = models.DateField()
    image = models.ImageField(
        upload_to=tools.get_users_image,
        verbose_name=("user image"),
        blank=True,
        null=True,
    )
    email = models.EmailField(
        ("email address"), max_length=255, unique=True, db_index=True
    )
    gender = models.CharField(
        choices=GENDER, verbose_name="cinsi", null=True, blank=False
    )

    #legacy fields
    old_psw_hash = models.CharField(blank=True, null=True, max_length=300)
    birth_date = models.DateField(blank=True, null=True)
    is_from_app = models.BooleanField(default=False)
    current_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    last_sign_in_ip = models.GenericIPAddressField(blank=True, null=True)
    sign_in_count = models.IntegerField(default=0)

    is_staff = models.BooleanField(
        ("staff status"),
        default=False,
        help_text=("Designates whether the user can log into this admin " "site."),
        db_index=True,
    )

    is_active = models.BooleanField(
        ("active"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )
    is_test = models.BooleanField(
        ("test user"),
        default=False,
        help_text =(
            "Designates whether this user was created by developers or not."
        )
    )
    date_joined = models.DateTimeField(("date joined"), default=timezone.now)
    last_activity = models.DateTimeField(("last activity"), blank=True, null=True)

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return "{full_name}".format(
            full_name=self.get_full_name(),
            email=self.get_username(),
        )
    
    def get_full_name(self):
        """
            Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        """
            Returns the short name for the user.
        """
        return self.first_name
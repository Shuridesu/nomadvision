from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from hashids import Hashids


# custom user manager class
class UserManager(BaseUserManager):
    # method for creating a normal user
    def create_user(self, email, password=None, **extra_fields):
        #veryfy if email is provided
        if not email:
            raise ValueError("Email address is required")

        # normalize email address
        email = self.normalize_email(email)
        email = email.lower()

        # create and save user model
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    # method for creating a superuser
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


# custom user account model
class UserAccount(AbstractBaseUser, PermissionsMixin):
    uid = models.CharField("uid", max_length=30, unique=True)
    email = models.EmailField("mail_address", max_length=255, unique=True)
    name = models.CharField("name", max_length=255)
    avatar = models.ImageField(
        upload_to="avatar", verbose_name="profile_photo", null=True, blank=True
    )
    introduction = models.TextField("introduction", null=True, blank=True)
    updated_at = models.DateTimeField("renewed_date", auto_now=True)
    created_at = models.DateTimeField("created_date", auto_now_add=True)

    #status field
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # ユーザーマネージャーと認証フィールドの設定
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = "user account"
        verbose_name_plural = "user accounts"

    def __str__(self):
        return self.name


#generate random uid for each user when user is created
@receiver(post_save, sender=UserAccount)
def generate_random_user_uid(sender, instance, created, **kwargs):
    if created:
        hashids = Hashids(salt="xRXSMT8XpzdUbDNM9qkv6JzUezU64D4Z", min_length=8)
        instance.uid = hashids.encode(instance.id)
        instance.save()

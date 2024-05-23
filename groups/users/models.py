from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from PIL import Image  # Ensure PIL is installed (pip install Pillow)
from django.contrib.auth import get_user_model


def upload_location(instance, filename):
    return f'profile_images/{filename}'


class UserManager(BaseUserManager):
    def create_user(self, email, password, profile_img=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=email, profile_img=profile_img)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, profile_img=None):
        user = self.create_user(email=email, password=password, profile_img=profile_img)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    profile_img = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=get_user_model())
def post_save_compress_img(sender, instance, *args, **kwargs):
    if instance.profile_img:
        picture = Image.open(instance.profile_img.path)
        picture.save(instance.profile_img.path, optimize=True, quality=30)

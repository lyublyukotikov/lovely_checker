from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLES = [
        ('admin', 'admin'),
        ('moderator', 'moderator'),
        ('simple_user', 'simple_user'),
        ('owner_user', 'owner_user'),
    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='userprofile'
    )
    fio = models.CharField(
        'fio',
        max_length=255,
        default='Ivanov Ivan Ivanovich'
    )
    phone_num = models.CharField(
        'phone_num',
        max_length=13,
        blank=True,
        null=True
    )
    photo = models.ImageField(
        'image',
        upload_to="users/%Y/%m/%d/",
        blank=True,
        null=True,
        default='images.png'
    )
    role = models.CharField(
        choices=ROLES,
        default='simple_user',
        max_length=255
    )

    def __str__(self):
        return f'Profile for user {self.user.username}'

    class Meta:
        verbose_name = 'Профиль юзера'
        verbose_name_plural = 'Профили юзеров'


class BecomeOwnerQuestionnaire(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    organisation_name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f'{self.organisation_name}'

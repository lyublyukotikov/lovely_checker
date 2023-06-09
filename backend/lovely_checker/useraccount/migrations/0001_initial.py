# Generated by Django 4.1.7 on 2023-03-12 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(default='Ivanov Ivan Ivanovich', max_length=255, verbose_name='fio')),
                ('phone_num', models.CharField(blank=True, max_length=13, null=True, verbose_name='phone_num')),
                ('photo', models.ImageField(blank=True, default='images.png', null=True, upload_to='users/%Y/%m/%d/', verbose_name='image')),
                ('role', models.CharField(choices=[('admin', 'admin'), ('moderator', 'moderator'), ('simple_user', 'simple_user'), ('owner_user', 'owner_user')], default='simple_user', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль юзера',
                'verbose_name_plural': 'Профили юзеров',
            },
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-25 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20180523_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='active',
        ),
        migrations.RemoveField(
            model_name='author',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_logged_in',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='activation_key',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name='author',
            name='email_validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

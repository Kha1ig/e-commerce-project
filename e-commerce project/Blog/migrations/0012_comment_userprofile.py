# Generated by Django 4.0.3 on 2022-04-18 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0011_remove_comment_parent_remove_comment_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
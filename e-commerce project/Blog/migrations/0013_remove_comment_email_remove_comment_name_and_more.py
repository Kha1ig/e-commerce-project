# Generated by Django 4.0.3 on 2022-04-23 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_comment_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='userprofile',
        ),
    ]
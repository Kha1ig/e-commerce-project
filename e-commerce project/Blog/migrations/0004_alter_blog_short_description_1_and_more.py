# Generated by Django 4.0.3 on 2022-04-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_author_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='short_description_1',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description_2',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description_3',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description_4',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description_5',
            field=models.TextField(max_length=250),
        ),
    ]

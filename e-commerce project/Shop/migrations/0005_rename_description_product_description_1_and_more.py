# Generated by Django 4.0.3 on 2022-04-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_alter_product_short_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='description_1',
        ),
        migrations.AddField(
            model_name='product',
            name='description_2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
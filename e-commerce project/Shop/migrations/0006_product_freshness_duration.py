# Generated by Django 4.0.3 on 2022-04-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_rename_description_product_description_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='freshness_duration',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-22 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0018_filter_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='filter_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.filter_price'),
        ),
    ]

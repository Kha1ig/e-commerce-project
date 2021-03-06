# Generated by Django 4.0.3 on 2022-04-06 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_product_freshness_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='packeting',
            field=models.CharField(choices=[('without touch of hand', 'Without touch of hand')], default='without touch of hand', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('no information', 'No information'), ("product doesn't exsist", "Product doesn't exsist"), ('in Stock', 'In Stock')], default='select', max_length=50),
        ),
    ]

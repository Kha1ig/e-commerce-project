# Generated by Django 4.0.3 on 2022-04-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product-image')),
                ('image_1', models.ImageField(upload_to='product-image')),
                ('image_2', models.ImageField(upload_to='product-image')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('select', 'Select'), ("product doesn't exsist", "Product doesn't exsist"), ('in Stock', 'In Stock')], max_length=50)),
                ('short_description', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('Depth', models.IntegerField()),
                ('Weight', models.IntegerField()),
                ('guarantee', models.CharField(max_length=50)),
                ('packeting', models.CharField(max_length=100)),
            ],
        ),
    ]

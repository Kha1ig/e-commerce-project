# Generated by Django 4.0.3 on 2022-05-03 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0011_rename_category_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='Brands',
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Products',
        ),
        migrations.AlterModelOptions(
            name='brands',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]

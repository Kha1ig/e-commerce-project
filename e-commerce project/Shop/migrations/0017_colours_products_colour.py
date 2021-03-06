# Generated by Django 4.0.3 on 2022-05-22 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0016_remove_order_customer_order_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Colour',
                'verbose_name_plural': 'Colours',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='colour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.colours'),
        ),
    ]

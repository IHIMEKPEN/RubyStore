# Generated by Django 3.2.8 on 2021-11-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ruby', '0006_auto_20211117_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cart_list',
            field=models.ManyToManyField(blank=True, related_name='users', to='Ruby.Product'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ruby', '0005_alter_user_cart_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cart_list',
        ),
        migrations.AddField(
            model_name='user',
            name='cart_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='Ruby.Product'),
        ),
    ]

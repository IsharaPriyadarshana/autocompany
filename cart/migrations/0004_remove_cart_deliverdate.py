# Generated by Django 4.1 on 2022-09-11 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_ordered_cart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='deliverDate',
        ),
    ]

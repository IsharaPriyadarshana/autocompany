# Generated by Django 4.1 on 2022-09-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='longDesc',
            field=models.TextField(default='This contains a detailed description of the product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]

# Generated by Django 3.1.4 on 2021-02-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210210_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]

# Generated by Django 4.1.1 on 2023-03-21 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
        migrations.AlterModelTable(
            name='product_image',
            table='product_image',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
        migrations.AlterModelTable(
            name='user_login',
            table='user_login',
        ),
        migrations.AlterModelTable(
            name='usercart',
            table='UserCart',
        ),
        migrations.AlterModelTable(
            name='usercartproduct',
            table='UserCartProduct',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='userprofile',
        ),
    ]

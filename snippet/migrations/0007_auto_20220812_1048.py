# Generated by Django 3.1.2 on 2022-08-12 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0006_pickup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['created'], 'permissions': (('manager_permission', 'Manager Permission'),)},
        ),
    ]

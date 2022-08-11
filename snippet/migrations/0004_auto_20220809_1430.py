# Generated by Django 3.1.2 on 2022-08-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0003_products_sales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='products',
            name='qty',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sales',
            name='estimation_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
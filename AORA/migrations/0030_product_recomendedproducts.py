# Generated by Django 4.1.5 on 2023-01-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0029_product_mechanismimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recomendedProducts',
            field=models.ManyToManyField(blank=True, to='AORA.product', verbose_name='Сопутствующие товары'),
        ),
    ]

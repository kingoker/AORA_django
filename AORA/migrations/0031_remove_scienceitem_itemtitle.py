# Generated by Django 4.1.5 on 2023-01-30 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0030_product_recomendedproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scienceitem',
            name='itemTitle',
        ),
    ]
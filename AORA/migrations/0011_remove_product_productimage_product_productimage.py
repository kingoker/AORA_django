# Generated by Django 4.1.5 on 2023-01-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0010_remove_contactinformation_page_topblock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productImage',
        ),
        migrations.AddField(
            model_name='product',
            name='productImage',
            field=models.ManyToManyField(to='AORA.productimage', verbose_name='Фотография продукта'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0027_remove_contactinformation_page_topblockheader_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productMainImage',
            field=models.ImageField(null=True, upload_to='products/', verbose_name='Главная картинка продукта'),
        ),
    ]

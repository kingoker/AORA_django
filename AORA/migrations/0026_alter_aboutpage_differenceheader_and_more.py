# Generated by Django 4.1.5 on 2023-01-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0025_remove_contactinformation_page_organization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='differenceHeader',
            field=models.CharField(max_length=255, verbose_name='Название отличий'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='differenceTitle',
            field=models.TextField(max_length=255, verbose_name='Заголовок отличий'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='scienceDescription',
            field=models.TextField(max_length=255, verbose_name='Заголовок науки'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='topBlockTitle',
            field=models.TextField(max_length=255, null=True, verbose_name='Верхний блок заголовок'),
        ),
        migrations.AlterField(
            model_name='differenceitem',
            name='itemDescription',
            field=models.TextField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='scienceitem',
            name='itemDescription',
            field=models.TextField(max_length=255, verbose_name='Описание'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0037_alter_contactinformation_page_sitenumber1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinformation_page',
            name='organizationTitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Загаловок над организаций'),
        ),
    ]

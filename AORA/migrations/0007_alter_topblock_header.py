# Generated by Django 4.1.5 on 2023-01-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0006_remove_innovationpage_innovationitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topblock',
            name='header',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
    ]

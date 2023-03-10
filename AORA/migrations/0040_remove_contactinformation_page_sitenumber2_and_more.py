# Generated by Django 4.1.5 on 2023-02-05 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0039_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinformation_page',
            name='sitenumber2',
        ),
        migrations.RemoveField(
            model_name='differenceitem',
            name='aboutPage',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='phoneNumber2',
        ),
        migrations.AddField(
            model_name='differenceitem',
            name='innovationPage',
            field=models.ForeignKey(blank=True, editable=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='AORA.innovationpage', verbose_name='Страница инноваций'),
        ),
    ]

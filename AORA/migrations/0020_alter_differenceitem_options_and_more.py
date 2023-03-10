# Generated by Django 4.1.5 on 2023-01-24 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0019_remove_aboutpage_topblock_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='differenceitem',
            options={'verbose_name': 'Наше отличие', 'verbose_name_plural': 'Наше отличие'},
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='differenceItem',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='mainImage',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='scienceItem',
        ),
        migrations.RemoveField(
            model_name='innovationpage',
            name='mainImage',
        ),
        migrations.AddField(
            model_name='differenceitem',
            name='aboutPage',
            field=models.ForeignKey(blank=True, editable=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='AORA.aboutpage', verbose_name='Страница о нас'),
        ),
        migrations.AddField(
            model_name='mainimage',
            name='aboutPage',
            field=models.ForeignKey(blank=True, editable=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='AORA.aboutpage', verbose_name='Страница о нас'),
        ),
        migrations.AlterField(
            model_name='differenceitem',
            name='itemImage',
            field=models.ImageField(upload_to='differenceItem/', verbose_name='Картинка или иконка'),
        ),
        migrations.CreateModel(
            name='ScienceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemImage', models.ImageField(upload_to='ScienceItem/', verbose_name='Картинка или иконка')),
                ('itemTitle', models.CharField(max_length=255, verbose_name='Название')),
                ('itemDescription', models.CharField(max_length=255, verbose_name='Описание')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('aboutPage', models.ForeignKey(blank=True, editable=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='AORA.aboutpage', verbose_name='Страница о нас')),
            ],
            options={
                'verbose_name': 'Научное сообщество',
                'verbose_name_plural': 'Научное сообщество',
            },
        ),
    ]

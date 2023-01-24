# Generated by Django 4.1.5 on 2023-01-24 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0018_remove_mainpage_topblock_topblock_contactpage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='topBlock',
        ),
        migrations.RemoveField(
            model_name='innovationpage',
            name='topBlock',
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='topBlockHeader',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Верхний блок название'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='topBlockImage',
            field=models.ImageField(null=True, upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='topBlockSubtitle',
            field=models.TextField(null=True, verbose_name='Верхний блок подзаголовок'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='topBlockTitle',
            field=models.CharField(max_length=255, null=True, verbose_name='Верхний блок заголовок'),
        ),
        migrations.AddField(
            model_name='contactinformation_page',
            name='topBlockHeader',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Верхний блок название'),
        ),
        migrations.AddField(
            model_name='contactinformation_page',
            name='topBlockImage',
            field=models.ImageField(null=True, upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка'),
        ),
        migrations.AddField(
            model_name='contactinformation_page',
            name='topBlockSubtitle',
            field=models.TextField(null=True, verbose_name='Верхний блок подзаголовок'),
        ),
        migrations.AddField(
            model_name='contactinformation_page',
            name='topBlockTitle',
            field=models.CharField(max_length=255, null=True, verbose_name='Верхний блок заголовок'),
        ),
        migrations.AddField(
            model_name='innovationpage',
            name='topBlockHeader',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Верхний блок название'),
        ),
        migrations.AddField(
            model_name='innovationpage',
            name='topBlockImage',
            field=models.ImageField(null=True, upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка'),
        ),
        migrations.AddField(
            model_name='innovationpage',
            name='topBlockSubtitle',
            field=models.TextField(null=True, verbose_name='Верхний блок подзаголовок'),
        ),
        migrations.AddField(
            model_name='innovationpage',
            name='topBlockTitle',
            field=models.CharField(max_length=255, null=True, verbose_name='Верхний блок заголовок'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='topBlockHeader',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Верхний блок название'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='topBlockImage',
            field=models.ImageField(null=True, upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='topBlockSubtitle',
            field=models.TextField(null=True, verbose_name='Верхний блок подзаголовок'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='topBlockTitle',
            field=models.CharField(max_length=255, null=True, verbose_name='Верхний блок заголовок'),
        ),
        migrations.DeleteModel(
            name='TopBlock',
        ),
    ]

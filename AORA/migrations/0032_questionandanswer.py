# Generated by Django 4.1.5 on 2023-01-30 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0031_remove_scienceitem_itemtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAndAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AORA.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Q&A',
                'verbose_name_plural': 'Q&A',
            },
        ),
    ]

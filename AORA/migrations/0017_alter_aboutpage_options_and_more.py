# Generated by Django 4.1.5 on 2023-01-23 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AORA', '0016_benefits_product_beneficiostext_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpage',
            options={'verbose_name': '- Страница О нас', 'verbose_name_plural': '- Страница О нас'},
        ),
        migrations.AlterModelOptions(
            name='contactinformation_page',
            options={'verbose_name': '- Страница Контакты', 'verbose_name_plural': '- Страница Контакты'},
        ),
        migrations.AlterModelOptions(
            name='differenceitem',
            options={'verbose_name': 'Элемент (картинка + текст)', 'verbose_name_plural': 'Элементы (картинка + текст)'},
        ),
        migrations.AlterModelOptions(
            name='innovationpage',
            options={'verbose_name': '- Страница Инноваций', 'verbose_name_plural': '- Страница Инноваций'},
        ),
        migrations.AlterModelOptions(
            name='mainpage',
            options={'verbose_name': '- Страница Главная', 'verbose_name_plural': '- Страница Главная'},
        ),
        migrations.AlterModelOptions(
            name='topblock',
            options={'verbose_name': 'Верхний блок', 'verbose_name_plural': 'Верхние блоки'},
        ),
        migrations.RemoveField(
            model_name='contactinformation_page',
            name='mainImage',
        ),
        migrations.RemoveField(
            model_name='mainpage',
            name='mainImage',
        ),
        migrations.AddField(
            model_name='mainimage',
            name='contactPage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AORA.contactinformation_page', verbose_name='Страница контакты'),
        ),
        migrations.AddField(
            model_name='mainimage',
            name='mainPage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AORA.mainpage', verbose_name='Страница главная'),
        ),
    ]

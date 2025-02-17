# Generated by Django 5.0.6 on 2024-06-20 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_lastname', models.CharField(max_length=255, verbose_name='Фамилия владельца')),
                ('owner_name', models.CharField(max_length=255, verbose_name='Имя владельца')),
                ('owner_surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество владельца')),
                ('location', models.CharField(max_length=255, verbose_name='Расположение')),
                ('capacity', models.PositiveIntegerField(default=10000, verbose_name='Вместимость')),
                ('main_delivery_type', models.CharField(choices=[('AP', 'Досталяется самолетом'), ('TR', 'Доставляется поездом'), ('TC', 'Доставляется фурами'), ('AL', 'Доступны все типы отправок')], default='AL', max_length=2, verbose_name='Способ отправки')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('rating', models.PositiveIntegerField(verbose_name='Оценка')),
                ('comment', models.TextField(verbose_name='Текст отзыва')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/review/%Y/%m/%d/', verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=2000, verbose_name='Количество')),
                ('mass', models.FloatField(verbose_name='Вес одного товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Товар')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.warehouse', verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Хранение позиции',
                'verbose_name_plural': 'Хранения позиций',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='warehouse',
            field=models.ManyToManyField(through='shop.Inventory', to='shop.warehouse', verbose_name='Склад'),
        ),
    ]

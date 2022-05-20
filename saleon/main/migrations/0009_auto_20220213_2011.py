# Generated by Django 3.1 on 2022-02-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220211_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='fullDiscrib',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='image1',
            field=models.ImageField(blank=True, upload_to='task/%Y/%m/%d/', verbose_name='Фото1'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='image2',
            field=models.ImageField(blank=True, upload_to='task/%Y/%m/%d/', verbose_name='Фото2'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='image3',
            field=models.ImageField(blank=True, upload_to='task/%Y/%m/%d/', verbose_name='Фото3'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='image',
            field=models.ImageField(blank=True, upload_to='task/%Y/%m/%d/', verbose_name='Фото превью'),
        ),
    ]
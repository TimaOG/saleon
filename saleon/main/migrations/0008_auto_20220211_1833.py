# Generated by Django 3.1 on 2022-02-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_tasks_promocod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='placeType',
            field=models.CharField(choices=[('KR', 'Кафе/ресторны'), ('M', 'Магазины'), ('R', 'Развлечения'), ('Z', 'Здоровье'), ('O', 'Остальное'), ('P', 'Путешествия')], max_length=250, verbose_name='Тип'),
        ),
    ]

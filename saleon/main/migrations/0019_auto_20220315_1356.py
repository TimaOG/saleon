# Generated by Django 3.1 on 2022-03-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_tasks_secondlinktext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='placeType',
            field=models.CharField(choices=[('KR', 'Кафе/ресторны'), ('M', 'Магазины'), ('R', 'Развлечения'), ('Z', 'Здоровье'), ('O', 'Остальное'), ('P', 'Путешествия'), ('Study', 'Учёба'), ('Car', 'Авто'), ('OneShop', 'Отдельные товары'), ('RECL', 'Реклама')], max_length=250, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='saleType',
            field=models.CharField(choices=[('Скидка', 'Скидка'), ('Кешбек', 'Кешбек'), ('Скидка до', 'Скидка до'), ('Кешбек до', 'Кешбек до'), ('Скидка от', 'Скидка от'), ('Кешбек от', 'Кешбек от')], default='Скидка', max_length=255, verbose_name='Вид скидки'),
        ),
    ]

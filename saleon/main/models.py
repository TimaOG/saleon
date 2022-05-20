from django.db import models
import datetime


class Tasks(models.Model):
    title = models.CharField('Название', max_length=250)
    image = models.ImageField('Фото превью', upload_to='task/%Y/%m/%d/', blank=True)
    image1 = models.ImageField('Фото1', upload_to='task/%Y/%m/%d/', blank=True)
    image2 = models.ImageField('Фото2', upload_to='task/%Y/%m/%d/', blank=True)
    image3 = models.ImageField('Фото3', upload_to='task/%Y/%m/%d/', blank=True)
    servis = models.CharField('Услуги', max_length=250)
    city = models.CharField('Город', max_length=255, blank=True)
    address = models.CharField('Адресс', max_length=250)
    metro = models.CharField('Метро', max_length=250)
    imageQR = models.ImageField('QR', upload_to='task/%Y/%m/%d/', blank=True)
    promoCod = models.CharField('Промокод', max_length=250, blank=True)
    sT = (('Скидка', 'Скидка'), ('Кешбек', 'Кешбек'), ('Скидка до', 'Скидка до'), ('Кешбек до', 'Кешбек до'), ('Скидка от', 'Скидка от'), ('Кешбек от', 'Кешбек от'))
    saleType = models.CharField('Вид скидки', max_length=255, choices=sT, default='Скидка')
    sale = models.IntegerField('Размер скидки')
    dateFor = models.CharField('Действрует до', max_length=255,blank=True)
    plT = (('KR', 'Кафе/ресторны'), ('M', 'Магазины'), ('R', 'Развлечения'), ('Z', 'Здоровье'), ('O', 'Остальное'), ('P', 'Путешествия'),
           ('Study', 'Учёба'), ('Car', 'Авто'), ('OneShop', 'Отдельные товары'), ('RECL', 'Реклама'))
    placeType = models.CharField('Тип',max_length=250, choices=plT)
    productLink = models.CharField('Ссылка на сайт', max_length=255, blank=True)
    mapLink = models.CharField('Ссылка на карту', max_length=255, blank=True)
    fullDiscrib = models.TextField('Описание', blank=True)
    ad = models.BooleanField('Реклама по категориям', default=False)
    secondLinkText = models.CharField('Текст дополнительной ссылки', max_length=255, default='Открыть страницу с предложением')
    secondLink = models.CharField('Дополнительная ссылка',max_length=255 ,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
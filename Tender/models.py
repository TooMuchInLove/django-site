#from django.db import models
from django.db.models import Model
from django.db.models import AutoField, ForeignKey
from django.db.models import CharField, DateTimeField, BooleanField, DecimalField
from django.db.models import SET_NULL, CASCADE


# Users
class User(Model):
    id = AutoField(primary_key=True)
    nameU = CharField(max_length=200, verbose_name='ФИО')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.nameU


# Regions
class Region(Model):
    id = AutoField(primary_key=True)
    nameR = CharField(max_length=100, unique=True, verbose_name='Регион')

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'регионы'

    def __str__(self):
        return self.nameR


# Tenders
class Tender(Model):
    id = AutoField(primary_key=True)
    regionFK = ForeignKey('Region', null=True, on_delete=SET_NULL, verbose_name='Регион')
    userAddFK = ForeignKey('User', null=True, on_delete=SET_NULL, verbose_name='Пользователь')
    numT = CharField(max_length=19, verbose_name='Номер')
    infoT = CharField(max_length=1000, null=True, verbose_name='Информация')
    dateAddT = DateTimeField(null=True, blank=True, verbose_name='Дата добавления')
    delT = BooleanField(default=False)
    startsSumT = DecimalField(max_length=23, null=True, blank=True, max_digits=20, decimal_places=2, verbose_name='Сумма')
    dateActionT = DateTimeField(null=True, blank=True, verbose_name='Дата подачи')
    dateDocT = DateTimeField(null=True, blank=True, verbose_name='Дата документа')
    zhnvlpT = BooleanField(default=False, verbose_name='ЖНВЛП')

    # unique - уникальность поля
    # auto_now- обновляет метку каждый раз при изменении (сохранении) строки в базе;
    # auto_now_add- создает метку при создании строки в базе.

    class Meta:
        verbose_name = 'тендер'
        verbose_name_plural = 'тендеры'

    def __str__(self):
        return self.numT
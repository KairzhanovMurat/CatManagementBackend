from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from . import managers


class Breed(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Владелец', on_delete=models.SET_NULL,
                              null=True, blank=True,
                              related_name='user_breeds')

    name = models.CharField(verbose_name='Название породы', max_length=255)
    description = models.TextField(verbose_name='Описание', max_length=1000,
                                   null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'


class Cat(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)
    age = models.IntegerField(verbose_name='Полных месяцев')
    color = models.CharField(verbose_name='Цвет', max_length=255)
    description = models.TextField(verbose_name='Описание', max_length=1000,
                                   null=True, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Владелец', on_delete=models.SET_NULL,
                              null=True, blank=True, related_name='users_cats')
    breeds = models.ManyToManyField('Breed', verbose_name='Породы', related_name='breed_cats')

    objects = managers.CatManager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'кошка'
        verbose_name_plural = 'кошки'


class CatRate(models.Model):
    rate = models.IntegerField(verbose_name='Оценка',
                               validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE,
                             related_name='user_rates')
    cat = models.ForeignKey('Cat', verbose_name='Кошка', on_delete=models.CASCADE,
                            related_name='cat_rates')

    def __str__(self):
        return f'{self.user} {self.cat}'

    class Meta:
        verbose_name = 'оценка'
        verbose_name_plural = 'оценки'

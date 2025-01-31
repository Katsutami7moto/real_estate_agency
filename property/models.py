from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Когда создано объявление',
        default=timezone.now,
        db_index=True
    )

    description = models.TextField(
        verbose_name='Текст объявления',
        blank=True
    )
    price = models.IntegerField(
        verbose_name='Цена квартиры',
        db_index=True
    )

    town = models.CharField(
        verbose_name='Город, где находится квартира',
        max_length=50,
        db_index=True
    )
    town_district = models.CharField(
        verbose_name='Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное'
    )
    address = models.TextField(
        verbose_name='Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4'
    )
    floor = models.CharField(
        verbose_name='Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж'
    )

    rooms_number = models.IntegerField(
        verbose_name='Количество комнат в квартире',
        db_index=True
    )
    living_area = models.IntegerField(
        verbose_name='количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True
    )

    has_balcony = models.NullBooleanField(
        verbose_name='Наличие балкона',
        db_index=True
    )
    active = models.BooleanField(
        verbose_name='Активно-ли объявление',
        db_index=True
    )
    construction_year = models.IntegerField(
        verbose_name='Год постройки здания',
        null=True,
        blank=True,
        db_index=True
    )
    new_building = models.BooleanField(
        verbose_name='Новостройка',
        null=True,
        default=None,
        db_index=True
    )

    liked_by = models.ManyToManyField(
        User,
        related_name="liked_flats",
        verbose_name='Кто лайкнул',
        default=None,
        blank=True
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Кто жаловался',
        related_name='complaints',
        null=True
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.SET_NULL,
        verbose_name='Квартира, на которую пожаловались',
        related_name='complaints',
        null=True
    )
    text = models.TextField(
        verbose_name='Текст жалобы'
    )

    def __str__(self) -> str:
        return f'Жалоба {self.user} на квартиру {self.flat}'


class Owner(models.Model):
    name = models.CharField(
        verbose_name='ФИО владельца',
        max_length=200,
        db_index=True
    )
    phonenumber = models.CharField(
        verbose_name='Телефон владельца',
        max_length=20,
        db_index=True
    )
    pure_phone = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name='Телефон владельца (нормализованный)',
        db_index=True
    )
    flats_owned = models.ManyToManyField(
        Flat,
        related_name='owners',
        verbose_name='Квартиры в собственности',
        db_index=True
    )

    def __str__(self) -> str:
        return f'{self.name}, {self.pure_phone}'

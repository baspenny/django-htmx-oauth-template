from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.currency.name} ({self.currency.code}) - {self.date}"


class License(models.Model):
    class LicenceTypeEnums(models.TextChoices):
        DV360 = 'Display & Video 360'

    name = models.CharField(max_length=255)
    platform_id = models.CharField(max_length=255)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=100,
        choices=LicenceTypeEnums.choices,
        default=LicenceTypeEnums.DV360
    )
    active = models.BooleanField(default=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Advertiser(models.Model):
    name = models.CharField(max_length=255)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    platform_id = models.CharField(max_length=255)
    license = models.ForeignKey(License, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vat(models.Model):
    code = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.country.name} - {self.country.code}"


class Client(models.Model):
    name = models.CharField(max_length=100)
    acumatica_id = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    account_director = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='account_director', null=True)
    account_manager = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='account_manager', null=True)
    sales_rep = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sales_rep', null=True, blank=True)
    vat = models.ForeignKey(Vat, on_delete=models.RESTRICT, verbose_name="VAT Code")
    def __str__(self):
        return self.name

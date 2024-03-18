from django.contrib import admin
from app.models import Currency, ExchangeRate, License, Advertiser, Country, Vat, Client


# Register your models here.
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Currency._meta.fields]


class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExchangeRate._meta.fields]


class LicenseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in License._meta.fields]


class AdvertiserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Advertiser._meta.fields]


class CountryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Country._meta.fields]


class VatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vat._meta.fields]


class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Advertiser, AdvertiserAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Vat, VatAdmin)
admin.site.register(Client, ClientAdmin)

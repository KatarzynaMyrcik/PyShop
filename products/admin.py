from django.contrib import admin
from .models import Product, Offer, Customers

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


class OffersAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


class CustomersAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "city")


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OffersAdmin)
admin.site.register(Customers, CustomersAdmin)

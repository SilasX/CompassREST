from django.contrib import admin

from api.models import Product, SellListing

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    pass


class SellListingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(SellListing, SellListingAdmin)

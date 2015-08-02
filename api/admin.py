from django.contrib import admin

from api.models import Product, SellListing, Location

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    pass


class SellListingAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(SellListing, SellListingAdmin)
admin.site.register(Location, LocationAdmin)

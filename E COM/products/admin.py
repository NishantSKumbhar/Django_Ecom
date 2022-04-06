from django.contrib import admin
from .models import Product, Discount

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'stock', 'price', 'user', 'import_date')

class DiscountAdmin(admin.ModelAdmin):
	list_display = ('off', 'coupon', 'purpose')


admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)

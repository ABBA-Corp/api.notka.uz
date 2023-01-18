from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from orzu.products.models import Product, ProductCategory, ProductCountry, Banners


@admin.register(Product)
class ProductAdmin(OrderedModelAdmin):
    raw_id_fields = ['category', 'country']
    list_display_fields = ['name']
    list_display = ('name', 'move_up_down_links', "thumbnail_preview")


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCountry)
class ProductCountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    pass

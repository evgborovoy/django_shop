from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = "product"
    model = Gallery
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "get_products_count")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}

    def get_products_count(self, obj):
        if obj.products:
            return str(len(obj.products.all()))
        else:
            return "0"

    get_products_count.short_description = "Quantity"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "quantity", "category", "size", "color", "get_image")
    list_display_links = ("pk", "title")
    list_editable = ("price", "quantity")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "price")
    inlines = (GalleryInline,)

    def get_image(self, obj):
        if obj.images.all():
            return mark_safe(f"<img src='{obj.images.all()[0].image.url}' width='75'>")
        else:
            return "-"

    get_image.short_description = "Image"

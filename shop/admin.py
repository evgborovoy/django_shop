from django.contrib import admin

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
    list_display = ("pk", "title", "price", "quantity", "category", "size", "color")
    list_display_links = ("pk", "title")
    list_editable = ("price", "quantity")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "price")
    inlines = (GalleryInline,)

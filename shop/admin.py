from django.contrib import admin

from .models import Category, Product, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = "product"
    model = Gallery
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "quantity", "category", "size", "color")
    list_display_links = ("pk", "title")
    list_editable = ("price", "quantity", "color", "size")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "price")
    inlines = (GalleryInline,)

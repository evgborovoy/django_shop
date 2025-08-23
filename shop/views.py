from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Product


class Index(ListView):
    model = Product
    extra_context = {"title": "Shop"}
    template_name = "shop/index.html"
    context_object_name = "categories"

    def get_queryset(self):
        categories = Category.objects.filter(parent=None)
        return categories


class SubCategories(ListView):
    model = Product
    context_object_name = "products"
    template_name = "shop/category_page.html"

    def get_queryset(self):
        parent_category = get_object_or_404(Category, slug=self.kwargs["slug"])
        products = Product.objects.filter(category__parent=parent_category).order_by("?")
        return products

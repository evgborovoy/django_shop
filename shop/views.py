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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["top_products"] = Product.objects.order_by("-watched")[:8]
        return context


class SubCategories(ListView):
    model = Product
    context_object_name = "products"
    template_name = "shop/category_page.html"

    def get_queryset(self):
        type_field = self.request.GET.get("type")
        if type_field:
            products = Product.objects.filter(category__slug=type_field)
            return products

        parent_category = get_object_or_404(Category, slug=self.kwargs["slug"])
        products = Product.objects.filter(category__parent=parent_category).order_by("?")

        sort_field = self.request.GET.get("sort")
        if sort_field:
            products = products.order_by(sort_field)
        return products

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data()
        parent_category = get_object_or_404(Category, slug=self.kwargs["slug"])
        context["category"] = parent_category
        context["title"] = parent_category.title
        return context

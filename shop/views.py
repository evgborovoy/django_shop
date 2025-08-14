from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Category, Product

class Index(ListView):
    model = Product
    extra_context = {"title": "Shop"}
    template_name = "shop/index.html"

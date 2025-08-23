from django import template
from shop.models import Category

register = template.Library()


@register.simple_tag()
def get_subcategories(category):
    return Category.objects.filter(parent=category)


@register.simple_tag()
def get_sorted():
    sorters = [
        {
            "title": "Price",
            "sorters": [
                ("price", "Increase"),
                ("-price", "Decrease"),
            ]
        },
        {
            "title": "Color",
            "sorters": [
                ("color", "Von a bis z"),
                ("-color", "Von z bis a"),
            ]
        },
        {
            "title": "Size",
            "sorters": [
                ("size", "Small - Large"),
                ("-size", "Large - Small"),
            ]
        },
    ]
    return sorters

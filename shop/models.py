from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="categories/", null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey("self",
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name="subcategories",
                               )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Category: {self.title}, pk={self.pk}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    watched = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    info = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField()
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Product: {self.title}, pk={self.pk}"


class Gallery(models.Model):
    image = models.ImageField(upload_to="products/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

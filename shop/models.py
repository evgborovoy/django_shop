from django.db import models
from django.urls import reverse


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

    def get_parent_photo(self):
        if self.image:
            return self.image.url
        else:
            return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fphoto-coming-soon-icon&psig=AOvVaw0lCL03bQtYz6HWm-kS6Ho8&ust=1755875232681000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCNDU1s6XnI8DFQAAAAAdAAAAABAV"

    def get_absolute_url(self):
        return reverse("shop:category_detail", kwargs={"slug": self.slug})


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

    def get_absolute_url(self):
        pass

    def get_first_photo(self):
        if self.images.first():
            return self.images.first().image.url
        else:
            return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fphoto-coming-soon-icon&psig=AOvVaw0lCL03bQtYz6HWm-kS6Ho8&ust=1755875232681000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCNDU1s6XnI8DFQAAAAAdAAAAABAV"


class Gallery(models.Model):
    image = models.ImageField(upload_to="products/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

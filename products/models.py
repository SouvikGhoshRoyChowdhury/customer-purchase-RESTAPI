from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    """
    Category Model For Product
    """

    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    """
    Product Model With Unique Name
    """

    name = models.CharField(max_length=50, unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    sold = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    label = models.CharField(max_length=20, null=True, blank=True)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.stock > 0:
            self.available = True
        else:
            self.available = False
        return super().save(*args, **kwargs)

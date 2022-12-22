from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, default='un-branded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
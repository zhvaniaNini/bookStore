from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    page_count = models.IntegerField()
    category = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.name
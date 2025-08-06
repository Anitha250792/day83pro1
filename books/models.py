from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percentage = models.PositiveIntegerField(default=0)  # 0-100

    def get_discounted_price(self):
        return self.price * (1 - self.discount_percentage / 100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[str(self.id)])

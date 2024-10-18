from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=240)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.PositiveIntegerField()
    authors = models.TextField(max_length=1500)
    publication = models.TextField(max_length=500)
    isbn = models.TextField(max_length=20)
    edition = models.TextField(max_length=50)
    edition_year = models.TextField(max_length=5)
    description = models.TextField(max_length=5000)
    book_conver = models.ImageField(upload_to='book_cover/', blank=True, null=True)
    tags = models.TextField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


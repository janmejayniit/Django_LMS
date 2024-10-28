from datetime import date, datetime, timedelta
from tkinter import CASCADE
from django.db import models


# from django.apps import apps

# Book = apps.get_model('ModBookApp', 'Book')

# Create your models here.
class Student(models.Model):
    first_name =  models.TextField(max_length=150,error_messages='First Name is required')
    last_name =  models.TextField(max_length=150)
    email = models.EmailField(max_length=240, unique=True)
    phone = models.BigIntegerField(unique=True)
    photo = models.ImageField(upload_to='student_photo/', blank=True, null=True)
    is_varified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def user_cover(self):
       return self.photo if self.photo else 'student_photo/Male_Avatar.jpg'
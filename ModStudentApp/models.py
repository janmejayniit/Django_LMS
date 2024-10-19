from datetime import date, datetime, timedelta
from tkinter import CASCADE
from django.db import models

from ModBookApp.models import Book

# Create your models here.
class Student(models.Model):
    first_name =  models.TextField(max_length=150)
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


class BookBorrow(models.Model):
    class FineFeeReasons(models.TextChoices):
        DELAY = 'Delay In Return'
        LOSS = 'Book Loss'
        DAMAAGE = 'Damage Book'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today)
    return_day = models.IntegerField(default=7)
    return_date = models.DateField(blank=True, null=True)
    fine_fee = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    reason_for_fine=models.CharField(max_length=50, choices=FineFeeReasons.choices, blank=True, null=True)

    def booksubmitdate(self):
        return self.issue_date + timedelta(days=self.return_day) 

    returnning_book_day = property(booksubmitdate)

    def brrowReturnStatus(self):
        flag = None
        
        if self.return_date is None: 
            if date.today()>self.returnning_book_day:
                flag = 'Fine'
            else:
                flag = 'Pending'
        else: 
            if self.returnning_book_day==self.return_date:
                flag = 'On Time Submit'
            elif self.returnning_book_day>self.return_date:
                flag = 'Early Submit'
            else:
                flag = 'Late Submit'
        return flag
    
    return_book_flag = property(brrowReturnStatus)
from django.db import models
from .models import BookBorrow, Student
from ModBookApp.models import Book
from django import forms

class BookBorrowForm(forms.ModelForm):
    class Meta:
        model = BookBorrow
        fields = ['student',  'book',  'issue_date',  'return_day']
        widgets = {
            'student': forms.Select(attrs={'class':'form-control'}, choices=[(student.first_name,student.id) for student in Student.objects.order_by('first_name').all()]),
            'book': forms.Select(attrs={'class':'form-control'},choices=[(book.title, book.id) for book in Book.objects.order_by('title').all()]),
            'issue_date':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'return_day':forms.NumberInput(attrs={'class':'form-control','max':15,'min':5})
        }
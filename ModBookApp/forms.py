from django import forms
from django.contrib.auth.models import User
from .models import Book
# from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title',  'price',  'pages',  'authors',  'publication',  'isbn',  'edition',  'edition_year',  'description',  'book_conver',  'tags' ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'authors':forms.TextInput(attrs={'class':'form-control'}),
            'publication':forms.TextInput(attrs={'class':'form-control'}),
            'isbn':forms.NumberInput(attrs={'class':'form-control'}),
            'edition':forms.TextInput(attrs={'class':'form-control'}),
            'edition_year':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control', 'rows':3,'title':'Description of book'}),
            'book_conver':forms.FileInput(attrs={'type':'file','class':'form-control'}),
            'tags':forms.TextInput(attrs={'class':'form-control'})
        }
        labels = {
            'title':'Book Name',
            'book_conver':'Upload Book Cover Image'
        }

# class BookForm(forms.Form):
#     title = forms.CharField(label='Book Full Name',widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
#     price = forms.CharField(label='Price', widget=forms.NumberInput(attrs={'class':'form-control'}), required=True)
#     pages = forms.CharField(label='Pages', widget=forms.NumberInput(attrs={'class':'form-control'}), required=True)
#     authors = forms.CharField(label='Authors Name', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
#     publication = forms.CharField(label='Publication Name', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
#     isbn = forms.CharField(label='ISBN Number', widget=forms.NumberInput(attrs={'class':'form-control'}), required=True)
#     edition = forms.CharField(label='Edition Volumne', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
#     edition_year = forms.CharField(label='Edition Year', widget=forms.NumberInput(attrs={'class':'form-control'}), required=True)
#     description = forms.CharField(label='Description (If any)', widget=forms.Textarea(attrs={'class':'form-control','row':'10'}), required=True)
#     book_cover = forms.CharField(label='Upload Book Cover Image', widget=forms.FileInput(attrs={'class':'form-control'}), required=True)
#     tags = forms.CharField(label='Tags for searching', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)


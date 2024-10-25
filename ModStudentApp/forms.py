# from django.db import models
from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    
    class Meta:
        model= Student
        fields = ['first_name','last_name','email','phone','photo']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'})
         }
         
    def clean(self):
        cleaned_date = super().clean()
        email = cleaned_date.get('email',None)
        phone = cleaned_date.get('phone',None) 

        if phone and Student.objects.filter(phone=phone).exists():
            # self.add_error('phone', 'Phone number is already taken')
            raise forms.ValidationError('Phone number is already in use')

        if len(str(phone))!=10:
            # self.add_error('phone','Phone must be 10 digit')
            raise forms.ValidationError('Phone must be of 10 digit')

        if Student.objects.filter(email=email).exists():
            # self.add_error('email', "Email already exists")
            raise forms.forms.ValidationError('Email is already in use')
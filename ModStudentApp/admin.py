from django.contrib import admin
from .models import Student

# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")

admin.site.register(Student, AdminStudent)

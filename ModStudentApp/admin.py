from django.contrib import admin
from .models import Student, BookBorrow

# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")

class AdminBookBorrow(admin.ModelAdmin):
    list_display = ("student", "book", "issue_date", "return_date")


admin.site.register(Student, AdminStudent)
admin.site.register(BookBorrow, AdminBookBorrow)

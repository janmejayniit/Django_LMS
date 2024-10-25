from django.contrib import admin
from .models import BookBorrow

# Register your models here.
class AdminBookBorrow(admin.ModelAdmin):
    list_display = ("student", "book", "issue_date", "return_date")

admin.site.register(BookBorrow, AdminBookBorrow)

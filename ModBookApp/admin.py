from django.contrib import admin
from .models import Book, BookStocks

# Register your models here.

class BookStockAdmin( admin.StackedInline):
    model=BookStocks
    list_display = ('book','total_books','available_books')
    max_num=1


class BookAdmin(admin.ModelAdmin):
  list_display = ("title", "authors", "isbn", "price", "pages")
  inlines = [
        BookStockAdmin,
    ]  

admin.site.register(Book, BookAdmin)
# admin.site.register(BookStocks, BookStockAdmin)



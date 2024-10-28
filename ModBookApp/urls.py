from .import views
from django.urls import path


urlpatterns = [
    path('', views.listBook, name='list_boook'),
    path('add_new/', views.addNew, name='add_new'),
    path('print_book_barcode/', views.printBookBarcode, name='print_book_barcode'),
    path('generate_barcode/', views.generateBarcode, name='generate_barcode'),
    path('export/csv/', views.export_csv, name='book_export_csv'),
    path('book_update/<int:bid>/', views.bookUpdate, name='book_update'),
    path('search/title/', views.searchBookTitle, name='book_title_search'),
]



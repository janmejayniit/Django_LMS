from .import views
from django.urls import path


urlpatterns = [
    path('', views.listBook, name='list_boook'),
    path('add_new/', views.addNew, name='add_new'),
    path('print_book_barcode/', views.printBookBarcode, name='print_book_barcode'),
    path('generate_barcode/', views.generateBarcode, name='generate_barcode'),
    # path('<int:tweet_id>/delete', views.tweet_delete, name='tweet_delete'),
]



from .import views
from django.urls import path


urlpatterns = [
    path('', views.listBook, name='list_boook'),
    path('add_new/', views.addNew, name='add_new')
    # path('<int:tweet_id>/delete', views.tweet_delete, name='tweet_delete'),
]



from .import views
from django.urls import path


urlpatterns = [
    path('', views.signin, name='signin'),
    path('logout/', views.signout , name='signout'),
]




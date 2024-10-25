"""
Django_LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.defaults import page_not_found

urlpatterns = [
    path('',include('ModAuthApp.urls')),
    path('book/', include('ModBookApp.urls')),
    path('student/', include('ModStudentApp.urls')),
     path('borrow/', include('ModBorrowApp.urls')),
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# def error_404(request, exception):
#     template_name = '404.html'
#     return page_not_found(request, exception, template_name=template_name)
 
# def error_500(request):
#     template_name = '500.html'
#     return page_not_found(request, template_name=template_name)


# handler404 = 'custom_views.handler404'
# handler500 = 'custom_views.handler500'
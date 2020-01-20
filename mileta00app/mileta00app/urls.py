from django.contrib import admin
from django.urls import path
from getmail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('unos/', views.unos, name='unos')
]

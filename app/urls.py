from django.contrib import admin
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home page'),
    path('register',views.register,name= 'register'),
    path('contact/', views.contact, name='contact'),
    path('search',views.search,name='search'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('blog', views.blog, name='blog'),


]

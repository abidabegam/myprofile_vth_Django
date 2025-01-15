# Django_testblog_project/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', views.home, name='home'),  # Home page
    path('<int:post_id>/', views.post_detail, name='post_detail'),  # Post detail page
    path('about/', views.about, name='about'),  # About page (new)
]

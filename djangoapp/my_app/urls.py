from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candies/', views.candies_index, name='candies_index'),
    path('candies/create/', views.candies_create, name='candies_create'),
    path('candies/<int:candy_id>/', views.candies_detail, name='candies_detail'),
]
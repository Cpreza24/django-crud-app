from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candies/', views.candies_index, name='candies_index'),
    path('candies/create/', views.candies_create, name='candies_create'),
    path('candies/<int:candy_id>/', views.candies_detail, name='candies_detail'),
    path('candies/<int:candy_id>/edit/', views.candies_edit, name='candies_edit'),
    path('candies/<int:candy_id>/delete/', views.candies_delete, name='candies_delete'),
    
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
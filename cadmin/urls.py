from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.login, {'template_name': 'cadmin/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'cadmin/logout.html'}, name='logout'),

    path('post/add/', views.post_add, name='post_add'), 
    path('post/update/<int:pk>/', views.post_update, name='post_update'), 
]
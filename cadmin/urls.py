from django.urls import path
from . import views

urlpatterns = [
    path('post/add/', views.post_add, name='post_add'), 
    path('post/update/<int:pk>/', views.post_update, name='post_update'), 
]
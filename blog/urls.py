from django.urls import path
from blog import views

urlpatterns = [
    path('time/', views.today_is, name='todays_time'), 
    path('', views.index, name='blog_index'), 
]
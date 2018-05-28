from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('activate/account/', views.activate_account, name='activate'),
    path('register/', views.register, name='register'), 
    path('password-change-done/', auth_views.password_change_done, 
          {'template_name':'cadmin/password_change_done.html'}, 
          name='password_change_done'),
    path('password-change/', auth_views.password_change,
          {'template_name':'cadmin/password_change.html', 'post_change_redirect':'password_change_done'}, 
          name='password_change'),
    path('', views.post_list, name='post_list'),  
    path('login/', views.login, {'template_name': 'cadmin/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'cadmin/logout.html'}, name='logout'),
    path('post/add/', views.post_add, name='post_add'), 
    path('post/update/<int:pk>/', views.post_update, name='post_update'), 
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('category/', views.category_list, name='category_list'),
    path('category/add/', views.category_add, name='category_add'),
    path('category/update/<int:pk>/', views.category_update, name='category_update'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('tag/', views.tag_list, name='tag_list'),
    path('tag/add/', views.tag_add, name='tag_add'),
    path('tag/update/<int:pk>/', views.tag_update, name='tag_update'),    
    path('tag/delete/<int:pk>/', views.tag_delete, name='tag_delete'),
    path('account-info/', views.account_info, name='account_info'),
]
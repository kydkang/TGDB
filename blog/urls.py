from django.urls import path
from blog import views

urlpatterns = [
    path('stop-tracking/', views.stop_tracking, name='stop_tracking'), 
    path('track_user/', views.track_user, name='track_user'), 
    path('cookie/', views.test_cookie, name='cooke'), 
    path('feedback/', views.feedback, name='feedback'), 
    path('blog/', views.test_redirect, name='test_redirect'), 
    path('category/<slug:category_slug>/', views.post_by_category, name='post_by_category'),
    path('tag/<slug:tag_slug>/', views.post_by_tag, name='post_by_tag'),  
#    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/<slug:post_slug>/', views.post_detail, name='post_detail'), 
    path('', views.post_list, name='post_list'), 
]
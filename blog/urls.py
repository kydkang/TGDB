from django.urls import path
from blog import views
from django.contrib.flatpages import views as flat_views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap

sitemaps = {
    'posts':PostSitemap
}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    path('about/', flat_views.flatpage, {'url': '/about/'}, name='about'),
    path(r'eula/', flat_views.flatpage, {'url': '/eula/'}, name='eula'),
    path('login/', views.login, name='blog_login'),
    path('logout/', views.logout, name='blog_logout'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('lousy-login/', views.lousy_login, name='lousy_login'),
    path('lousy-secret/', views.lousy_secret, name='lousy_secret'),
    path('lousy-logout/', views.lousy_logout, name='lousy_logout'),
    path('save-session-data/', views.save_session_data, name='save_session_data'),
    path('access-session-data/', views.access_session_data, name='access_session_data'),
    path('delete-session-data/', views.delete_session_data, name='delete_session_data'),
    path('test-delete/', views.test_delete, name='test_delete'),
    path('test-session/', views.test_session, name='test_session'),
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
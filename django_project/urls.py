from django.contrib import admin
from django.urls import path
from django.conf.urls import include 

urlpatterns = [
    path('', include('blog.urls')),  
    path('admin/', admin.site.urls),  
    path('cadmin/', include('cadmin.urls')), 
]

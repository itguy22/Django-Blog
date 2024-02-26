# cmsapp/urls.py
from django.contrib import admin
from django.urls import path, include
from blog.views import PostListView  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', PostListView.as_view(), name='home'),  # Point the root URL to the PostListView
]

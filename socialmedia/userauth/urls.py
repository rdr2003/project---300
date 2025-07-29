from django.contrib import admin
from django.urls import path
from socialmedia import settings
from userauth import views
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home),
    path('loginn/',views.loginn),
    path('signup/',views.signup),
    path('logoutt/',views.logoutt),
    path('upload',views.upload),
    path('like-post/<str:id>', views.likes, name='like-post'),
    path('#<str:id>', views.home_post),
    path('explore',views.explore),
    path('profile/<str:id_user>', views.profile),
    path('delete/<str:id>', views.delete),
    path('search-results/', views.search_results, name='search_results'),
    path('follow', views.follow, name='follow'), 
    path('post-job/', views.post_job, name='post_job'),
    path('jobs/', views.view_jobs, name='view_jobs'),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='settings'),
    
    
    
]

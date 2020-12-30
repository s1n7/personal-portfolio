from django.urls import path
from . import views     #imports blog app views.py file

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),    #if integer entered after "blog/"

]

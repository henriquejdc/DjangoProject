from django.urls import path, include
from . import views


app_name = 'comments'


urlpatterns = [
    path('', views.comments_home, name='comments_home'),
]

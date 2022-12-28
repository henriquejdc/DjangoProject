from django.urls import path, include
from . import views


app_name = 'comments'


urlpatterns = [
    path('', views.comments_home, name='comments_home'),
    path('profile/<slug:username>/', views.get_user_profile_add_comment, name='get_user_profile_add_comment'),
    path('details/<int:id_comment>/', views.comment_details, name='comment_details'),
]

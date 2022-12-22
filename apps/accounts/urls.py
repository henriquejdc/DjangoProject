from django.urls import path, include
from . import views


app_name = 'accounts'


urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('profile/', views.create_profile, name='create_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.AddUserCreateView.as_view(), name='add_user'),
]

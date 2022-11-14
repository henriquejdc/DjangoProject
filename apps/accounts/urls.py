from django.urls import path, include
from . import views


app_name = 'accounts'


urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login_user'),
    path('create/', views.AddUserCreateView.as_view(), name='add_user'),
]

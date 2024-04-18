from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.index, name="index"),
    path('sign-up', views.signup_form, name="sign-up"),
    path('login-page', views.login_form, name="login-page"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user-logout', views.user_logout, name="user-logout"),
]

from django.urls import path
from .views import reg, profile
from django.contrib.auth import views as authv

urlpatterns = [
    path('', reg, name='reg'),
    path('profile/', profile, name='profile'),
    path('auth/', authv.LoginView.as_view(template_name='users/auth.html'), name='auth'),
    path('exit/', authv.LogoutView.as_view(template_name='users/logout.html'), name='exit')
]
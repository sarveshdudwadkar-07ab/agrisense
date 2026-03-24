from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register_view, dashboard_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('change/', views.ChangePassword.as_view(), name='change_password'),
    path('reset/', views.ResetPassword.as_view(), name='reset_password'),
]
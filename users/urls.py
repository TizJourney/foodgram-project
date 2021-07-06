from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import (PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('change/', views.ChangePassword.as_view(), name='change_password'),
    path('reset/', views.ResetPassword.as_view(), name='reset_password'),
    path(
        'password_reset/', PasswordResetView.as_view(
            form_class=PasswordResetForm,
            template_name='users/changePassword.html',
            subject_template_name='commons/password_reset_subject.txt',
            email_template_name='commons/password_reset_email.html',
            success_url='follow',), name="password_reset"),

    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='users/changePassword.html'),
        name="password_reset_done"
    ),

    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/PasswordResetConfirm.html',
        ), name="password_reset_confirm"
    ),

    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='users/changePasswordComplete.html'),
        name="password_reset_complete"
    ),
]

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import forget, login_view, register_user
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_view

urlpatterns = [
   
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset_password/", auth_view.PasswordResetView.as_view(), name="reset_password"),
    path("reset_password_sent/", auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete/", auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
  
]

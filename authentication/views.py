# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import ForgetForm, LoginForm, SignUpForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            # return redirect("/curso/")
            if user is not None:
                login(request, user)
                return redirect("curso")
            else:    
                msg = 'DATOS NO VALIDOS'    
        else:
            msg = 'ERROR AL VALIDAR LOS DATOS DLE FORMULARIO'    

    return render(request, "./accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'USUARIO CREADO <a href="/login">login</a>.'
            success = True
            
            return redirect("/login/")

        else:
            msg = 'FORMULARIO NO ES VALIDO'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })



def forget(request):

    msg     = None
    success = False

    if request.method == "PUT":
        form = ForgetForm(request.PUT)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'CONTRASEÑA MODIFICADA <a href="/login">login</a>.'
            success = True
            
            return redirect("/login/")

        else:
            msg = 'FORMULARIO NO ES VALIDO'    
    else:
        form = ForgetForm()

    return render(request, "accounts/page-reset-password.html", {"form": form, "msg" : msg, "success" : success })

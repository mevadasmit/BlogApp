from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic import View
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from constant import (POST, USERNAME, USER_LOGIN, ACCOUNT_CREATED, FORM, CHANGE_PASSWORD, PASSWORD_UPDATED,
                      ERROR_CORRECTION, PROFILE_UPDATED, USER_PROFILE, U_UPDATE_FORM, P_UPDATE_FORM)


# Create your views here.

def register(request):
    if request.method == POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get(USERNAME)
            messages.success(request, ACCOUNT_CREATED.format(username=username))
            return redirect(USER_LOGIN)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {FORM: form})


def logoutview(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required()
def change_password(request):
    if request.method == POST:
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, PASSWORD_UPDATED)
            return redirect(CHANGE_PASSWORD)
        else:
            messages.error(request, ERROR_CORRECTION)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        FORM: form
    })


@login_required
def profile(request):
    if request.method == POST:

        u_update_form = UserUpdateForm(request.POST, instance=request.user)
        p_update_form = ProfileUpdateForm(request.POST, request.FILES
                                          , instance=request.user.profile)

        if u_update_form.is_valid() and p_update_form.is_valid():
            u_update_form.save()
            p_update_form.save()
            messages.success(request, PROFILE_UPDATED)
            return redirect(USER_PROFILE)
    else:
        u_update_form = UserUpdateForm(instance=request.user)
        p_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        U_UPDATE_FORM: u_update_form,
        P_UPDATE_FORM: p_update_form
    }

    return render(request, 'users/profile.html', context)

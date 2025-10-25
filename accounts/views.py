from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegistrationForm
from dashboard.models import ProgrammingLog


def sign_up_view(request):
    """ Handles User registration """
    form = RegistrationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        ProgrammingLog.ensure_user_logs(user)
        return redirect('dashboard:dashboard')

    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_in_view(request):
    """ Handles User login """
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('dashboard:dashboard')

    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_out_view(request):
    """ Handles User logout"""
    if request.user.is_authenticated:
        logout(request)
    return redirect('sign_in')

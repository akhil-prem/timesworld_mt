from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from .models import AppUser
from .permissions import is_student_or_admin, is_staff_or_admin, is_editor_or_admin, is_admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages


def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/profile')
                return redirect(next_url)
            else:
                messages.error(
                    request, 'Invalid username or password. Please try again.')
    return render(request, "auth/login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('/login')


def register(request):
    success = False
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            messages.success(
                request, 'Registration has been completed successfully - Please <a href="/login"><u>login</u></a>')
    else:
        form = RegistrationForm()
    return render(request, "auth/register.html", {"form": form, "success": success})


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
@user_passes_test(is_student_or_admin, login_url='/access-denied/')
def students(request):
    users = AppUser.objects.filter(role='student')
    page = 'students'
    return render(request, 'user_list.html', {'users': users, 'page': page})


@login_required
@user_passes_test(is_staff_or_admin, login_url='/access-denied/')
def staffs(request):
    users = AppUser.objects.filter(role='staff')
    page = 'staffs'
    return render(request, 'user_list.html', {'users': users, 'page': page})


@login_required
@user_passes_test(is_admin, login_url='/access-denied/')
def admins(request):
    users = AppUser.objects.filter(role='admin')
    page = 'admins'
    return render(request, 'user_list.html', {'users': users, 'page': page})


@login_required
@user_passes_test(is_editor_or_admin, login_url='/access-denied/')
def editors(request):
    users = AppUser.objects.filter(role='editor')
    page = 'editors'
    return render(request, 'user_list.html', {'users': users, 'page': page})


def access_denied(request):
    return render(request, 'page-403.html')

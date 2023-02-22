from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    check_user = request.user.is_authenticated
    if check_user:
        return redirect('home:home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')

    return render(request, 'account/login.html', context={})


def logout_view(request):
    logout(request)
    return redirect('home:home')


def register_view(request):
    context ={'errors': []}

    check_user = request.user.is_authenticated
    if check_user:
        return redirect('home:home')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        if User.objects.get(username=username):
            context['errors'].append('This username exists.')
            return render(request, 'account/register.html', context=context)
        if password != confirm_password:
            context['errors'].append('Passwords do not match.')
            return render(request, 'account/register.html', context=context)
        user = User.objects.create(username=username, email=email, password=password)
        login(request, user)
        return redirect('home:home')

    return render(request, 'account/register.html', context={})

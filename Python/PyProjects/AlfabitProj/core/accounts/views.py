from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'accounts/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            authenticated_user = authenticate(
                request, email=email, password=password)

            if authenticated_user is not None:
                request.user = authenticated_user
                request.session.save()  
                return redirect('index')
            else:
                form.add_error(None, "Неверное имя или пароль")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

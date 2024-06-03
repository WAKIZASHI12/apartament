from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 and password2 and password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Имя пользователя уже занято.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Этот email уже используется.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, f'Ваш аккаунт был создан! Вы можете войти, {username}.')
                return redirect('login') 
        else:
            messages.error(request, 'Пароли не совпадают.')
        
    return render(request, 'register/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Заменить 'home' на имя  URL для домашней страницы
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль.')
    
    return render(request, 'accounts/login.html')
def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        email = request.POST.get('email')
        if email:
            user.email = email
            user.save()
            messages.success(request, 'Ваш профиль был обновлен!')
            return redirect('profile')
    return render(request, 'accounts/profile.html') 
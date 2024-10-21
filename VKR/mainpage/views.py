from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required


def mainpage(request):
    # Если пользователь уже вошел, перенаправляем его на основную страницу приложения
    if request.user.is_authenticated:
        return redirect('mainapplication_view')  # Перенаправление на основную страницу
    return render(request, 'mainpage/mainpage.html')  # Отображаем главную страницу для неавторизованных пользователей

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('mainapplication_view')  # Перенаправление на основную страницу после регистрации
    else:
        form = CustomUserCreationForm()

    return render(request, 'mainpage/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user)
            return redirect('mainapplication_view')  # Переход на основную страницу после входа
    else:
        form = CustomAuthenticationForm()
    return render(request, 'mainpage/login.html', {'form': form})

@login_required
def mainapplication_view(request):
    return render(request, 'mainapplication/mainapplication.html', {'user': request.user})

def logout_view(request):
    logout(request)  # Выход из системы
    return redirect('mainpage')  # Перенаправление на главную страницу
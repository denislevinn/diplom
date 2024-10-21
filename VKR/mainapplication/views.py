from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def mainapplication_view(request):
    users = User.objects.exclude(id=request.user.id)  # Исключаем текущего пользователя
    return render(request, 'mainapplication/mainapplication.html', {'users': users})


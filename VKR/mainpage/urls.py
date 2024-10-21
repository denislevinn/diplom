from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),  # Измените имя здесь
    path('logout/', views.logout_view, name='logout_view'),  # Выход

]

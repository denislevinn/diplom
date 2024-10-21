from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainapplication_view, name='mainapplication_view'),
]

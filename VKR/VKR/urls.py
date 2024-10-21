from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),
    path('main/', include('mainapplication.urls')),  # маршруты основного приложения

]

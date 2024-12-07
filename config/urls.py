"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index, delete, detail, add, toggle_task_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('add', add, name='add'),
    path('task/toggle/<int:pk>/', toggle_task_status, name='toggle_task_status'),
]


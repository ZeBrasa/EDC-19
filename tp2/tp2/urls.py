"""tp1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path

from app import views
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='static/ico/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^favicon\.ico$', favicon_view),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about/$', views.about, name='about'),
    path('add_org/', views.add_org, name='add_org'),
    path('<path:selection>', views.element, name='element'),
]
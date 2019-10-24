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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', views.home, name='home'),
    path('about/', views.about, name='about'),
    url(r'^continents/$', views.continents, name='continents'),
    url(r'^countries/$', views.countries, name='countries'),
    path('organizations/', views.organizations, name='organizations'),
    path('list/', views.list, name='list'),
    url(r'^(?P<prev>[-\w]+)/(?P<selection>[-\w]+)', views.list, name='list'),
    path('rss/', views.rss, name='rss'),
]
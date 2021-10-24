"""bookmanage02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from book import views

from django.urls import converters,register_converter

class PhoneConverter:
    regex = '1[3-9][0-9]{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
register_converter(PhoneConverter,'phone')


urlpatterns = [
    path('', views.index, name='主页'),
    path('index/', views.index, name='主页'),
    path('<int:a>/<phone:b>/', views.urla),
    path('head/', views.heads),
    path('res/', views.resq),
    path('set_cookie/', views.set_cookies),
    path('get_cookie/', views.get_cookie),
    path('set_session/', views.set_session),
    path('get_session/', views.get_session),
    path('method/',views.GetView.as_view())
]


"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from untitled2 import wsgi
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('regist/', wsgi.regist),
#     path('login/', wsgi.login),
#     path('logout', wsgi.logout),
# ]

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from cmdb import views
urlpatterns = [
  url(r'addstu/', login_required(views.regist)),
  url(r'login/', login_required(views.dglogin)),
  url(r'index/', login_required(views.index)),
]

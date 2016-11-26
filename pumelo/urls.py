"""pumelo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from eslone import views as eslone_views
from eslone import tests as eslone_tests
urlpatterns = [
    url(r'^add/',eslone_tests.db_add),
    url(r'^read/',eslone_tests.db_read),
    url(r'^$',eslone_views.index),
    url(r'^admin/', admin.site.urls),
]
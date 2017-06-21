"""turtle_control URL Configuration

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
from django.contrib.auth.views import logout
from app.views import index, control_panel_t, control_panel_d, index_register, index_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^index/', index, name="index"),
    url(r'^control_panel_t/', control_panel_t, name="control_panel_t"),
    url(r'^control_panel_d/', control_panel_d, name="control_panel_d"),
    url(r'^register/$', index_register, name="register"),
    url(r'^login/$', index_login, name="login"),
    url(r'^logout/', logout, {'next_page': '/index'}, name="logout"),
]

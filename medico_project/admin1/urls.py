"""medico_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path,include
from . import views
urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path("icons/", views.icons, name="icons"),
    path("map/", views.map, name="map"),
    path("maps/", views.maps, name="maps"),
    path("notifications/", views.notifications, name="notifications"),
    path("rtl/", views.rtl, name="rtl"),
    path("tables/", views.tables, name="tables"),
    path("typography/", views.typography, name="typography"),
    path("upgrade/", views.upgrade, name="upgrade"),
    path("user/", views.user, name="user"),
    path("template/", views.template, name="template"),
    ]

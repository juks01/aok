"""
URL configuration for aok project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from aok.views import Main, Members
from news.views import News
from events.views import Events, Slots
from discord_oauth2 import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view(), name='main'),
    path('members/', Members.as_view(), name='members'),
    path('news/', News.as_view(), name='news'),
    path('events/', Events.as_view(), name='events'),
    path("events/<int:id>/", Slots.as_view(), name="event"),
    path("oauth2/", include("discord_oauth2.urls")),
#    path('', views.frontpage, name='main'),
]

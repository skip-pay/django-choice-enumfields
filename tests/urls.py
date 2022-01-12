# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import path, include
import django
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    path(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = staticfiles_urlpatterns() + urlpatterns

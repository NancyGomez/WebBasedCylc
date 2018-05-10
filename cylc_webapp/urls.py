from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^register', views.register, name='register'),
    url(r'^suites', views.suites, name='suites'),
    url(r'^suite_view', views.suite_view, name='suite_view')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#this is for dev, should be changed for production
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.search),
    re_path(r'^(?P<input>[\w-]+)/$', views.detail)
]

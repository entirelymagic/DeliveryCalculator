from django.contrib import admin
from django.urls import path, include
from .views import IndexPageView


app_name = 'calculator'


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
]
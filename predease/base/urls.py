from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('base/about.html',views.about, name='about'),
]
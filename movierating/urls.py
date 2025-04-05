from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path("__reload__/", include("django_browser_reload.urls")),

]
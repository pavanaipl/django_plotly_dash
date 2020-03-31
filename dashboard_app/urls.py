from django.urls import path
from . import views
from dashboard_app.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.home, name='home'),
    path('testing/', views.testing),

]

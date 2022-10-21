from django.urls import path

from . import views

app_name = 'osoby'
urlpatterns = [
    path('', views.index, name='lista'),
    path('info/', views.info, name='info'),
]

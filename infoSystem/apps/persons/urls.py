from django.urls import path
from . import views

app_name = 'persons'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('create/', views.create_page, name='create_page'),
    path('add/', views.create, name='create')
]
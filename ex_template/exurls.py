from django.urls import path
from . import views

app_name = 'ex_template'

urlpatterns = [
    path('', views.index, name='index'),
    path('ex01/', views.ex01, name = 'ex01'),
    path('ex02/', views.ex02, name = 'ex02'),
    path('ex03/', views.ex03, name = 'ex03'),
]
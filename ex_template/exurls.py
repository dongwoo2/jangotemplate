from django.urls import path
from . import views

app_name = 'ex_template'

urlpatterns = [
    path('', views.index, name='index'),
]
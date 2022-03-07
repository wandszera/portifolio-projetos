from django.urls import path

from . import views

app_name = 'projetos'

urlpatterns = [
    path('adicionar/', views.add_category, name='add_category'),
    path('adicionar/projeto', views.add_projeto, name='add_projeto'),
    path('list/', views.list_projeto, name='list_projeto'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='usuario_list'),
    path('usuario/<int:pk>/', views.post_detail, name='usuario_detail'),
    path('usuario/new/', views.post_new, name='usuario_new'),
    path('usuario/edit/<int:pk>/', views.post_edit, name='usuario_edit'),
    path('usuario/delete/<int:pk>/', views.delete, name='usuario_delete')
]
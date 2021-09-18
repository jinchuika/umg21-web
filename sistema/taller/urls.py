from . import views
from django.urls import include, path

urlpatterns = [
    path('cliente/', views.ClienteListView.as_view(), name='cliente_list'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('cliente/add/', views.ClienteCreateView.as_view(), name='cliente_add'),
    path('cliente/<int:pk>/edit/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
]

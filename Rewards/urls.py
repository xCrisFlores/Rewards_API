from django.urls import path
from . import views

urlpatterns = [
    path('compras/', views.create_purchase, name='create_purchase'),
    path('compras/<str:user>/', views.list_user_purchases, name='list_user_purchases'),
    path('puntos/<str:user>/', views.calculate_rewards, name='calculate_rewards'),
]
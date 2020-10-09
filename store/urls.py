from django.urls import path
from . import views
from .views import (
    ProductListView,
    ProductDetailView
)

urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product"),
    path('checkout/', views.checkout, name="checkout"),
]

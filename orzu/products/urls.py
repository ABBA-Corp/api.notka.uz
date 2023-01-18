from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path('mymodels/', ProductViewSet.as_view(), name='product-list'),
]

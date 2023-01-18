from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from orzu.products.views import ProductViewSet, ProductCategoryListView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("products", ProductViewSet)

app_name = "api"
urlpatterns = router.urls
urlpatterns += [
    path("categories/", ProductCategoryListView.as_view(), name="category_list"),
]

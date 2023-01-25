from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from orzu.news.views import NewsViewSet
from orzu.products.views import ProductViewSet, ProductCategoryListView, ProductBannerListView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("products", ProductViewSet)
router.register("news", NewsViewSet)
router.register("banners", ProductBannerListView)
router.register("categories", ProductCategoryListView)

app_name = "api"
urlpatterns = router.urls

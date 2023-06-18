from cgitb import lookup
from django.urls import include, path
from caketake import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
# router.register("product", views.productViewSet, basename="product")
router.register("customershop", views.cshopViewSet, basename="shop")
router.register("address", views.addressViewSet)
router.register("seller", views.sellerViewSet)
router.register("customer", views.customerViewSet)
router.register("order", views.orderViewSet, basename="order")
router.register("fps", views.fpsViewSet)
# router.register("Shop", views.ShopViewSet, basename="Shop")

shop = routers.NestedDefaultRouter(router, "customershop", lookup="shop")
shop.register("product", views.productViewSet, basename="customershop-product")


# shop = routers.NestedDefaultRouter(router, "shop", lookup="shop")
# shop.register("fps", views.fpsViewSet, basename="product-fps")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(shop.urls)),
    path("shops/", views.ShopList.as_view()),
    path("shops/product/", views.productList.as_view()),
]

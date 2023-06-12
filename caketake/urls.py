from cgitb import lookup
from django.urls import include, path
from caketake import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
# router.register("product", views.productViewSet, basename="product")
router.register("shop", views.shopViewSet, basename="shop")
router.register("address", views.addressViewSet)
router.register("seller", views.sellerViewSet)
router.register("customer", views.customerViewSet)
router.register("order", views.orderViewSet, basename="order")
router.register("fps", views.fpsViewSet)

shop = routers.NestedDefaultRouter(router, "shop", lookup="shop")
shop.register("product", views.productViewSet, basename="shop-product")

# product_router = routers.NestedDefaultRouter(router, "product", lookup="product")
# item_router = routers.NestedDefaultRouter(router, "bag", lookup="bag")
# item_router.register("items", views.items, basename="bag-items")
urlpatterns = [
    path("", include(router.urls)),
    path("", include(shop.urls)),
    # path("", include(product_router.urls)),
    # path("", include(item_router.urls))
]

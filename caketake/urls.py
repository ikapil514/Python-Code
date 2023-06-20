from django.urls import include, path
from caketake import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
# router.register("product", views.productViewSet, basename="product")
router.register("customershop", views.cshopViewSet, basename="shop")
router.register("sellershop", views.sellershopViewSet, basename="sshop")
router.register("address", views.addressViewSet)
router.register("seller", views.sellerViewSet)
router.register("customer", views.customerViewSet)
router.register("order", views.orderViewSet, basename="order")
router.register("fps", views.fpsViewSet)
# router.register("Shop", views.ShopViewSet, basename="Shop")

shop = routers.NestedDefaultRouter(router, "customershop", lookup="shop")
shop.register("product", views.productViewSet, basename="customershop-product")

sellershop = routers.NestedDefaultRouter(router, "sellershop", lookup="shop")
sellershop.register(
    "product", views.sellerproductViewSet, basename="sellershop-product"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(shop.urls)),
    path("", include(sellershop.urls)),
    # path("shops/", views.ShopList.as_view()),
    # path("shops/product/", views.productList.as_view()),
]

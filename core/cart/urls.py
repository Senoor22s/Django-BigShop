from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("session/add-product/",views.SessionAddProduct.as_view(),name="session-add-product"),
    path("session/cart/summary/",views.SessionCartSummary.as_view(),name="session-cart-summary"),
    path("session/remove-product/",views.SessionRemoveProductView.as_view(),name="session-remove-product"),
    path("session/update-product-quantity/",views.SessionUpdateProductQuantityView.as_view(),name="session-update-product-quantity"),
]
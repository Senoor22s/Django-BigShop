from django.urls import path
from . import views

app_name = "admin"

urlpatterns = [
    path("home/",views.AdminDashboardHomeView.as_view(),name="home"),
    path("secuirty-edit/",views.AdminSecurityEditView.as_view(),name="security-edit"),
    path("profile-edit/",views.AdminProfileEditView.as_view(),name="profile-edit"),
    path("profile/image/edit/",views.AdminProfileImageEditView.as_view(),name="profile-image-edit"),
    path("product/list/",views.AdminProductListView.as_view(),name="product-list"),
    path("product/<int:pk>/edit/",views.AdminProductEditView.as_view(),name="product-edit"),
    path("product/<int:pk>/delete/",views.AdminProductDeleteView.as_view(),name="product-delete"),
    path("product/create/",views.AdminProductCreateView.as_view(),name="product-create"),
    path("newsletter/list/",views.NewsLetterListView.as_view(),name="newsletter-list"),
    path("newsletter/<int:pk>/delete/",views.NewsLetterDeleteView.as_view(),name="newsletter-delete"),
    path("ticket/list/",views.TicketListView.as_view(),name="ticket-list"),
    path("ticket/<int:pk>/edit/",views.TicketEditView.as_view(),name="ticket-edit"),
    path("ticket/<int:pk>/delete/",views.TicketDeleteView.as_view(),name="ticket-delete"),
    path("user/list/",views.UserListView.as_view(),name="user-list"),
    path("user/<int:pk>/edit/",views.UserEditView.as_view(),name="user-edit"),
    path("user/<int:pk>/delete/",views.UserDeleteView.as_view(),name="user-delete"),
    path("order/list/",views.AdminOrderListView.as_view(),name="order-list"),
    path("order/<int:pk>/detail/",views.AdminOrderDetailView.as_view(),name="order-detail"),
    path("order/<int:pk>/invoice/",views.AdminOrderInvoiceView.as_view(),name="order-invoice"),
]
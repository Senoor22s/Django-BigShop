from django.urls import path
from . import views

app_name = "admin"

urlpatterns = [
    path("home/",views.AdminDashboardHomeView.as_view(),name="home"),
    path("secuirty-edit/",views.AdminSecurityEditView.as_view(),name="security-edit"),
    path("profile-edit/",views.AdminProfileEditView.as_view(),name="profile-edit"),
    path("profile/image/edit/",views.AdminProfileImageEditView.as_view(),name="profile-image-edit"),
    path("product/list/",views.AdminProductListView.as_view(),name="product-list")
]
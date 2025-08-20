from django.views.generic import TemplateView,UpdateView,ListView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.admin.forms import AdminPasswordChangeForm,AdminProfileEditForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from accounts.models import Profile
from django.shortcuts import redirect
from django.contrib import messages
from shop.models import ProductModel,ProductCategoryModel
from django.core.exceptions import FieldError
from .forms import ProductForm
from website.models import Newsletter,Contact
from website.forms import ContactForm

class AdminDashboardHomeView(LoginRequiredMixin,HasAdminAccessPermission,TemplateView):
    template_name = "dashboard/admin/home.html"


class AdminSecurityEditView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = "dashboard/admin/profile/security-edit.html"
    form_class = AdminPasswordChangeForm
    success_url = reverse_lazy("dashboard:admin:security-edit")
    success_message = "بروز رسانی پسورد با موفقیت انجام شد"

class AdminProfileEditView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/admin/profile/profile-edit.html"
    form_class = AdminProfileEditForm
    success_url = reverse_lazy("dashboard:admin:profile-edit")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)


class AdminProfileImageEditView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names=["post"]
    model = Profile
    fields= [
        "image"
    ]
    success_url = reverse_lazy("dashboard:admin:profile-edit")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطفا مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)

class AdminProductListView(LoginRequiredMixin, HasAdminAccessPermission,ListView):
    template_name = "dashboard/admin/products/product-list.html"
    paginate_by = 10
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size',self.paginate_by)

    def get_queryset(self):
        queryset = ProductModel.objects.all()
        if search_q:=self.request.GET.get("q"):
            queryset = queryset.filter(title__icontains=search_q)
        if category_id:=self.request.GET.get("category_id"):
            queryset = queryset.filter(category__id=category_id)
        if min_price:= self.request.GET.get("min_price"):
            queryset = queryset.filter(price__gte=min_price)
        if max_price:= self.request.GET.get("max_price"):
            queryset = queryset.filter(price__lte=max_price)
        if order_by:= self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        context["categories"] = ProductCategoryModel.objects.all()        
        return context

class AdminProductEditView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/admin/products/product-edit.html"
    queryset = ProductModel.objects.all()
    form_class = ProductForm
    success_message = "ویرایش محصول با موفقیت انجام شد"
    
    def get_success_url(self):
        return reverse_lazy("dashboard:admin:product-edit",kwargs={"pk":self.get_object().pk})

class AdminProductDeleteView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/admin/products/product-delete.html"
    queryset = ProductModel.objects.all()
    success_url = reverse_lazy("dashboard:admin:product-list")
    success_message = "حذف محصول با موفقیت انجام شد"

class AdminProductCreateView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/admin/products/product-create.html"
    queryset = ProductModel.objects.all()
    form_class = ProductForm
    success_message = "ایجاد محصول با موفقیت انجام شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy("dashboard:admin:product-list")

class NewsLetterListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    template_name = "dashboard/admin/newsletter/newsletter-list.html"
    def get_queryset(self):
        return Newsletter.objects.all().order_by("-id")

class NewsLetterDeleteView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    model = Newsletter
    template_name = "dashboard/admin/newsletter/newsletter-delete.html"
    success_url = reverse_lazy("dashboard:admin:newsletter-list")
    success_message = "حذف خبرنامه با موفقیت انجام شد"

class TicketListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    template_name = "dashboard/admin/ticket/ticket-list.html"
    def get_queryset(self):
        return Contact.objects.all().order_by("-id")

class TicketDeleteView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    model = Contact
    template_name = "dashboard/admin/ticket/ticket-delete.html"
    success_url = reverse_lazy("dashboard:admin:ticket-list")
    success_message = "حذف تیکت با موفقیت انجام شد"

class TicketEditView(LoginRequiredMixin, HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/admin/ticket/ticket-edit.html"
    queryset = Contact.objects.all()
    form_class = ContactForm
    success_message = "ویرایش تیکت با موفقیت انجام شد"

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:ticket-edit",kwargs={"pk":self.get_object().pk})

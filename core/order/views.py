from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasCustomerAccessPermission
from order.models import UserAddressModel
from .forms import CheckOutForm
from cart.models import CartModel
from django.urls import reverse_lazy

class OrderCheckOutView(LoginRequiredMixin, HasCustomerAccessPermission,FormView):
    template_name = "order/checkout.html"
    form_class = CheckOutForm
    success_url = reverse_lazy('order:completed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        context["addresses"] = UserAddressModel.objects.filter(user=self.request.user)
        total_price = cart.calculate_total_price()
        total_tax = round((total_price * 9)/100)
        context["total_price"] = total_price
        context["total_tax"] = total_tax
        context["total_last_price"] = total_price + total_tax
        return context
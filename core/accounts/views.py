from django.contrib.auth import views as auth_views
from .forms import AuthenticationForm
from django.contrib import messages

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "شما با موفقیت وارد شدید.")
        return response

class LogoutView(auth_views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "شما با موفقیت خارج شدید.")
        return super().dispatch(request, *args, **kwargs)

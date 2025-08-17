from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import NewsletterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ContactForm

class IndexView(TemplateView):
    template_name = "website/index.html" 

class ContactView(TemplateView):
    template_name = "website/contact.html" 
    
class AboutView(TemplateView):
    template_name = "website/about.html" 

class NewsletterView(SuccessMessageMixin,FormView):
    template_name = 'website/index.html'
    form_class = NewsletterForm
    success_url = reverse_lazy('website:index')
    success_message = "عضویت در خبرنامه با موفقیت انجام شد"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ContactView(FormView):
    template_name = "website/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("website:contact")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "با موفقیت ارسال شد")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "مشکلی در ارسال پیش آمد ، مجددا تلاش کنید")
        return super().form_invalid(form)
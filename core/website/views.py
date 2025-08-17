from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import NewsletterForm
from django.contrib.messages.views import SuccessMessageMixin

class IndexView(TemplateView):
    template_name = "website/index.html" 

class ContactView(TemplateView):
    template_name = "website/contact.html" 
    
class AboutView(TemplateView):
    template_name = "website/about.html" 

class NewsletterView(SuccessMessageMixin,FormView):
    template_name = 'index.html'
    form_class = NewsletterForm
    success_url = reverse_lazy('website:index')
    success_message = "عضویت در خبرنامه با موفقیت انجام شد"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
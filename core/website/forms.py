from django import forms
from website.models import Newsletter
from .models import Contact

class NewsletterForm(forms.ModelForm):

    class Meta:
        model=Newsletter
        fields='__all__'

class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact
        fields='__all__'
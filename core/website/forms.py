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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control '
        self.fields['phone_number'].widget.attrs['class'] = 'form-control '
        self.fields['email'].widget.attrs['class'] = 'form-control '
        self.fields['phone_number'].widget.attrs['class'] = 'form-control '  
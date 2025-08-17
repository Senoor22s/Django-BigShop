from django import forms
from website.models import Newsletter

class NewsletterForm(forms.ModelForm):

    class Meta:
        model=Newsletter
        fields='__all__'
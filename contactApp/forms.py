from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    """Form definition for Contact."""
    contact = forms.CharField(required=True)
    email = forms.EmailField(required=False)


    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = ('name', 'contact', 'email', 'location',)
    
    

        




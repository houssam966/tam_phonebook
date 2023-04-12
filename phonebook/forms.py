from django import forms
from django.forms import formset_factory
from .models import Contact, PhoneNumber

class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name']
    
    phone_numbers = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        contact = super().save(commit)
        numbers = self.cleaned_data['phone_numbers'].split('\n')
        for number in numbers:
            PhoneNumber.objects.create(contact=contact, number=number.strip())
        return contact
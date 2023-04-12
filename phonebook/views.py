from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import AddContactForm

def add_contact(request):
    if request.method == 'POST':
        form = AddContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phonebook:list_contacts')
    else:
        form = AddContactForm()
    return render(request, 'phonebook/add_contact.html', {'form': form})

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'phonebook/list_contacts.html', {'contacts': contacts})

def contact_details(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'phonebook/contact_details.html', {'contact': contact})


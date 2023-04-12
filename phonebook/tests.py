from django.test import TestCase
from django.urls import reverse

from .models import Contact

class ContactModelTest(TestCase):
    def test_contact_creation(self):
        contact = Contact.objects.create(name='John Doe')
        self.assertEqual(str(contact), 'John Doe')

class PhonebookViewTest(TestCase):
    def test_contact_list_view(self):
        url = reverse('phonebook:list_contacts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_contact_view(self):
        url = reverse('phonebook:add_contact')
        data = {'name': 'Jane Doe', 'number': '123-456-7890, 098-765-4321'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_contact_detail_view(self):
        contact = Contact.objects.create(name='John Doe')
        url = reverse('phonebook:contact_details', args=[contact.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_invalid_contact_detail_view(self):
        url = reverse('phonebook:contact_details', args=[12345])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_add_contact_duplicate_name(self):
        # Adding a contact with the same name as an existing contact should fail
        Contact.objects.create(name='John Doe')
        url = reverse('phonebook:add_contact')
        data = {'name': 'John Doe', 'number': '123-456-7890'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact with this Name already exists.')

    def test_add_contact_no_name(self):
        # Adding a contact with no name should fail
        url = reverse('phonebook:add_contact')
        data = {'number': '123-456-7890'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
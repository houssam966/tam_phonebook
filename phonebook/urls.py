from django.urls import path

from . import views

app_name = 'phonebook'

urlpatterns = [
    path('add_contact/', views.add_contact, name='add_contact'),
    path('', views.list_contacts, name='list_contacts'),
    path('<int:contact_id>/', views.contact_details, name='contact_details'),
]
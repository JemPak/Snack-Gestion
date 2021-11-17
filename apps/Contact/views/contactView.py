#imports of Django and res_framework
from django.db.models import query
from apps.Contact.models.contact import Contact
from rest_framework import generics, views

#imports of serializers
from apps.Contact.serializers.contactSerializer import ContactSerializer

class ContactIsActiveView(generics.ListAPIView):
    queryset = Contact.objects.filter(is_active=True)
    serializer_class = ContactSerializer

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



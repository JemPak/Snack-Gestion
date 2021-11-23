#imports of Django and rest_framework
from apps.Contact.models.contact import Contact
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

#imports of serializers
from apps.Contact.serializers.contactSerializer import ContactSerializer

class ContactIsActiveView(generics.ListAPIView):
    queryset = Contact.objects.filter(is_active=True)[:10]
    serializer_class = ContactSerializer

class ContactUser(generics.ListAPIView):
    serializer_class = ContactSerializer
    
    def get_queryset(self):
        if self.kwargs["active"] != "active" and self.kwargs["active"] != "inactive":
            stringResponse = {'detail':'Unauthorized Request'}
            get_object_or_404 (Contact, user_id="00") 
            return Response(stringResponse, status=status.HTTP_404_NOT_FOUND)
        ACTIVO = True if self.kwargs["active"] == "active" else False
        queryset = Contact.objects.filter(user_id=self.kwargs["user_id"], is_active=ACTIVO)
        return queryset

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



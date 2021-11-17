#imports of Django and res_framework
from apps.Installation.models.installation import Installation
from rest_framework import generics
from rest_framework.response import Response

#imports of serializers
from apps.Installation.serializers.installationSerializer import InstallationSerializer

class InstallationListCreateView(generics.ListCreateAPIView):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer

class InstallationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
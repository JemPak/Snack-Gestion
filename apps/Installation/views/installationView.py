#imports of Django and res_framework
from apps.Installation.models.installation import Installation
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

#imports of serializers
from apps.Installation.serializers.installationSerializer import InstallationSerializer

class InstallationIsAcceptedView(generics.ListAPIView):
    queryset = Installation.objects.filter(accepted=False)[:10]
    serializer_class = InstallationSerializer

class InstallationUser(generics.ListAPIView):
    serializer_class = InstallationSerializer
    
    def get_queryset(self):
        if self.kwargs["active"] != "accepted" and self.kwargs["active"] != "unaccepted":
            stringResponse = {'detail':'Unauthorized Request'}
            get_object_or_404 (Installation, user_id="00") 
            return Response(stringResponse, status=status.HTTP_404_NOT_FOUND)
        ACCEPTED = True if self.kwargs["active"] == "accepted" else False
        queryset = Installation.objects.filter(user_id=self.kwargs["user_id"], accepted=ACCEPTED)
        return queryset

class InstallationListCreateView(generics.ListCreateAPIView):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer

class InstallationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
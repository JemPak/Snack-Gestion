from django.db.models import fields
from rest_framework import serializers
from apps.Installation.models import Installation

class InstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = '__all__'
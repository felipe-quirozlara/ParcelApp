from django.db.models import fields
from rest_framework import serializers
from parcel.models import Envio

class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = '__all__'
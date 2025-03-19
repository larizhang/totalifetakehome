from rest_framework import serializers
from .models import Clinician, Appointment, Patient

class ClinicianSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=30)
    npi = serializers.IntegerField()
    email = serializers.EmailField()

    # creates and returns the clinician object
    def create(self, validated_data):
        return Clinician.objects.create(**validated_data)
    
    # updates the clinician object with new data
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.npi = validated_data.get('npi', instance.npi)
        instance.state = validated_data.get('state', instance.state)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
class PatientSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    dob = serializers.DateField()
    email = serializers.EmailField()
    address = serializers.CharField(max_length=200)

    # creates and returns the patient object
    def create(self, validated_data):
        return Clinician.objects.create(**validated_data)
    
    # updates the patient object with new data
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class AppointmentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    provider = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()

    # returns the nested clinician object
    def get_provider(self, obj):
        provider = ClinicianSerializer(obj.provider).data
        return provider
    
    # returns the nested client object
    def get_client(self, obj):
        client = PatientSerializer(obj.client).data
        return client

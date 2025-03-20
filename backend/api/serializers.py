from rest_framework import serializers
from .models import Clinician, Appointment, Patient

class ClinicianSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=30)
    npi = serializers.IntegerField()
    email = serializers.EmailField()

    class Meta:
        model = Clinician
        fields = "__all__"

    # creates and returns the clinician object
    def create(self, validated_data):
        return Clinician.objects.create(**validated_data)
    
    # checks if NPI is length of 10 digits
    def validate_npi(self, value):
        if len(str(value)) != 10:
            raise serializers.ValidationError("NPI value is not 10 digits long")
        return value

    # ensures email is unique for clinician
    def validate_email(self, value):
        if Clinician.objects.filter(email=value):
            raise serializers.ValidationError("Email is already registered for a clinician")
        return value
    
    # updates the clinician object with new data
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.npi = validated_data.get('npi', instance.npi)
        instance.state = validated_data.get('state', instance.state)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
class PatientSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    dob = serializers.DateField()
    email = serializers.EmailField()
    address = serializers.CharField(max_length=200)

    class Meta:
        model = Patient
        fields = "__all__"

    # ensures email is unique for patient
    def validate_email(self, value):
        if Patient.objects.filter(email=value):
            raise serializers.ValidationError("Email is already registered for a patient")
        return value

    # creates and returns the patient object
    def create(self, validated_data):
        return Patient.objects.create(**validated_data)
    
    # updates the patient object with new data
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class AppointmentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    provider = ClinicianSerializer()
    client = PatientSerializer()
    date = serializers.DateField()
    time = serializers.TimeField()
    status = serializers.ChoiceField(choices=Appointment.APPOINTMENT_STATUSES)

    # broken at the moment, cannot nest objects properly without creating new patient/clinician objects
    # addition through the admin terminal still works
    class Meta:
        model = Appointment
        fields = "__all__"

    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)

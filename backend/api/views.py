from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import Clinician, Patient, Appointment
from .serializers import ClinicianSerializer, PatientSerializer, AppointmentSerializer

import requests, json

# gets and returns all clinician object data
@api_view(["GET"])
def get_clinicians(request):
    clinicians = Clinician.objects.all()
    data = {}
    serializer = ClinicianSerializer(clinicians, many=True)
    data['providers'] = serializer.data
    return Response(data)

# creates a new clinician object
@api_view(["POST"])
def create_clinician(request):
    if request.method == "POST":
        serializer = ClinicianSerializer(data=request.data)
        if serializer.is_valid():
            npi_request = requests.get("https://npiregistry.cms.hhs.gov/api/?number={number}&version=2.1".format(number = serializer.validated_data["npi"]))
            npi_data = json.loads(npi_request.text)
            if npi_data["result_count"] == 1:
                state = npi_data["results"][0]["addresses"][0]["state"]
                first_name = npi_data["results"][0]["basic"]["first_name"].lower().capitalize()
                last_name = npi_data["results"][0]["basic"]["last_name"].lower().capitalize()
                if first_name != serializer.validated_data["first_name"]:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"first_name": ["First name does not match registry information"]})
                elif last_name != serializer.validated_data["last_name"]:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"last_name": ["Last name does not match registry information"]})
                elif state != serializer.validated_data["state"]:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"state": ["State does not match registry information"]})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"npi": ["NPI could not be found in registry"]})

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

# creates, updates and deletes any clinician object
@api_view(["GET", "PUT", "DELETE"])
def get_update_and_delete_clinician(request, id):
    # TODO validate NPI here with requests
    if request.method == "GET":
        clinician = get_object_or_404(Clinician, id=id)
        serializer = ClinicianSerializer(clinician)
        return Response(serializer.data)
    elif request.method == "PUT":
        clinician = get_object_or_404(Clinician, id=id)
        serializer = ClinicianSerializer(clinician, data=request.data)
        if serializer.is_valid():
            npi_request = requests.get("https://npiregistry.cms.hhs.gov/api/?number={number}&version=2.1".format(number = serializer.validated_data["npi"]))
            npi_data = json.loads(npi_request.text)
            if npi_data["result_count"] == 1:
                state = npi_data["results"][0]["addresses"][0]["state"]
                first_name = npi_data["results"][0]["basic"]["first_name"].lower().capitalize()
                last_name = npi_data["results"][0]["basic"]["last_name"].lower().capitalize()
                if first_name != serializer.validated_data["first_name"]:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"first_name": ["First name does not match registry information"]})
                elif last_name != serializer.validated_data["last_name"]:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"last_name": ["Last name does not match registry information"]})
                elif state != serializer.validated_data["state"]:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={"state": ["State does not match registry information"]})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"npi": ["NPI could not be found in registry"]})

            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        clinician = get_object_or_404(Clinician, id=id)
        clinician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

# gets and returns all appointment object data
@api_view(["GET"])
def get_appointments(request):
    appointments = Appointment.objects.all()
    data = {}
    serializer = AppointmentSerializer(appointments, many=True)
    data['appointments'] = serializer.data
    return Response(data)

# creates a new appointment object
@api_view(["POST"])
def create_appointment(request):
    if request.method == "POST":
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


# creates, updates and deletes any appointment object
@api_view(["GET", "PUT", "DELETE"])
def get_update_and_delete_appointment(request, id):
    if request.method == "GET":
        appointment = get_object_or_404(Appointment, id=id)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    elif request.method == "PUT":
        appointment = get_object_or_404(Appointment, id=id)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        appointment = get_object_or_404(Appointment, id=id)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

# gets and returns all patient object data
@api_view(["GET"])
def get_patients(request):
    patients = Patient.objects.all()
    data = {}
    serializer = PatientSerializer(patients, many=True)
    data['clients'] = serializer.data
    return Response(data)

# creates a new patient object
@api_view(["POST"])
def create_patient(request):
    if request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


# creates, updates and deletes any patient object
@api_view(["GET", "PUT", "DELETE"])
def get_update_and_delete_patient(request, id):
    if request.method == "GET":
        patient = get_object_or_404(Patient, id=id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    elif request.method == "PUT":
        patient = get_object_or_404(Patient, id=id)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        patient = get_object_or_404(Patient, id=id)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
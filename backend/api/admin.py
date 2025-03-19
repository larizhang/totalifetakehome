from django.contrib import admin
from .models import Patient, Clinician, Appointment

# Register your models here.

admin.site.register(Patient)
admin.site.register(Clinician)
admin.site.register(Appointment)
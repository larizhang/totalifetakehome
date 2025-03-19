from django.db import models

# TODO SET many attributes to NOT NULL

class Clinician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    npi = models.IntegerField("Identification number for healthcare providers")
    email = models.EmailField(unique=True)

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField("Date of birth")
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)

class Appointment(models.Model):
    APPOINTMENT_STATUSES = {
        "booked" : "Booked",
        "completed": "Completed",
        "cancelled" : "Cancelled",
        "rescheduled": "Rescheduled"
    }

    provider = models.ForeignKey(Clinician, on_delete=models.CASCADE)
    client = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField("Date scheduled")
    time = models.TimeField("Time scheduled")
    status = models.CharField(max_length=15, default="booked",choices=APPOINTMENT_STATUSES)
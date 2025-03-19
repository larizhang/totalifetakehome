from django.urls import path

from . import views

# all api endpoints
urlpatterns = [
    path("clinicians/", views.get_clinicians, name="get_clinicians"),
    path("clinicians/create/", views.create_clinician, name="create_clinician"),
    path("clinicians/<int:id>/", views.get_update_and_delete_clinician, name="get_update_and_delete_clinician"),
    path("patients/", views.get_patients, name="get_patients"),
    path("patients/create/", views.create_patient, name="create_patient"),
    path("patients/<int:id>/", views.get_update_and_delete_patient, name="get_update_and_delete_patient"),
    path("appointments/", views.get_appointments, name="get_appointments"),
    path("appointments/create/", views.create_appointment, name="create_appointment"),
    path("appointments/<int:id>/", views.get_update_and_delete_appointment, name="get_update_and_delete_appointment"),
]
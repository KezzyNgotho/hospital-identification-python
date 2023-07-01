from django.contrib.auth.backends import BaseBackend

from central_identification.central_identification.models import Student,Person
""" from .models import Person """

class biometric_auth_backend(BaseBackend):
    def authenticate(self, request, fingerprint=None, eye_data=None, face_data=None, voice_data=None):
        try:
            person = Person.objects.get(fingerprint=fingerprint, eye_data=eye_data, face_data=face_data, voice_data=voice_data)
            return person.student  # Return the associated student object if authentication succeeds
        except Person.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None

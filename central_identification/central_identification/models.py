from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fingerprint = models.TextField()
    eye_data = models.TextField()
    face_data = models.TextField()
    voice_data = models.TextField()
    dna_data = models.TextField()
    location = models.CharField(max_length=100)

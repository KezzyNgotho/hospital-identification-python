from django.db import models

class Person(models.Model):
    fingerprint = models.TextField()
    eye_data = models.TextField()
    face_data = models.TextField()
    voice_data = models.TextField()
    dna_data = models.TextField()
    location = models.CharField(max_length=100)

class Student(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=100, default='0001')
    username = models.CharField(max_length=100)
    # Add other fields as needed for the attendance application

    def __str__(self):
        return self.username

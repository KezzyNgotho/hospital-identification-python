from django.shortcuts import render, redirect
from .models import Person, Student
from django.contrib.auth import authenticate, login

def home_view(request):
    return render(request, 'home.html')

def collect_data(request):
    if request.method == 'POST':
        # Process the form data and save it to the database
        fingerprint = request.POST.get('fingerprint')
        eye_data = request.POST.get('eye_data')
        face_data = request.POST.get('face_data')
        voice_data = request.POST.get('voice_data')
        dna_data = request.POST.get('dna_data')
        location = request.POST.get('location')

        person = Person(
            fingerprint=fingerprint,
            eye_data=eye_data,
            face_data=face_data,
            voice_data=voice_data,
            dna_data=dna_data,
            location=location
        )
        person.save()

        # Render a success message or redirect to another page
        return render(request, 'success.html')

    # Render the data collection form
    return render(request, 'data_collection.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Student

def login(request):
    if request.method == 'POST':
        fingerprint = request.POST.get('fingerprint')
        eye_data = request.POST.get('eye_data')
        face_data = request.POST.get('face_data')
        voice_data = request.POST.get('voice_data')

        user = authenticate(request, fingerprint=fingerprint, eye_data=eye_data, face_data=face_data, voice_data=voice_data)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Biometric authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid biometric data'})

    # Render the login template
    return render(request, 'login.html')


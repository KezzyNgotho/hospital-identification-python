from django.shortcuts import render, redirect
from .models import Person

def home_view(request):
    return render(request, 'home.html')

def collect_data(request):
    if request.method == 'POST':
        # Process the form data and save it to the database
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        fingerprint = request.POST.get('fingerprint')
        eye_data = request.POST.get('eye_data')
        face_data = request.POST.get('face_data')
        voice_data = request.POST.get('voice_data')
        dna_data = request.POST.get('dna_data')
        location = request.POST.get('location')

        person = Person(
            first_name=first_name,
            last_name=last_name,
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

def login(request):
    if request.method == 'POST':
        # Perform the login authentication logic here
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Add your authentication code here

        # If the login is successful, redirect to the home view
        return redirect('home')

    # Render the login template
    return render(request, 'login.html')

from django.urls import path
from central_identification.views import home_view, collect_data
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('press-start-data-collection/', collect_data, name='data_collection'),
    path('', home_view, name='home'),
    path('collect-data/', collect_data, name='collect_data'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # Other URL patterns...
]

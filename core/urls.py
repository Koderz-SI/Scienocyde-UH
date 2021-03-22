from django.urls import path
from core.views import about, projects, contact, host, add_host, host_dashboard, detail, applyto, participant, add_participant

urlpatterns = [
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('host/', host, name='host'),
    path('host/add_host/', add_host, name='add_host'),
    path('host_dashboard/', host_dashboard, name='host_dashboard'),
    path('detail/', detail , name='detail'),
    path('applyto/', applyto , name='applyto'),
    path('participant/', participant , name='participant'),
    path('participant/add_participant/', add_participant, name='add_participant'), 
]

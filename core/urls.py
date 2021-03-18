from django.urls import path
from core.views import about, projects, contact, host, add_host

urlpatterns = [
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('host/', host, name='host'),
    path('host/add_host/', add_host, name='add_host'),
]

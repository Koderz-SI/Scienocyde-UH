from django.urls import path
from core.views import about, projects, contact, host

urlpatterns = [
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('host/', host, name='host'),
]

from django.shortcuts import render, redirect
from django.http import HttpResponse

def about(request):
	template_name = "core/about.html"
	return render(request, template_name)

def projects(request):
	template_name = "core/projects.html"
	return render(request, template_name)

def contact(request):
	template_name = "core/contact.html"
	return render(request, template_name)

def host(request):
	template_name = "core/host.html"
	return render(request, template_name)
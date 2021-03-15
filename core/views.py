from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import HostForm

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
	form=HostForm()
	context = {'app_name': "Scienocyde-UH", 'form': form}
	
	return render(request, template_name , context=context)

def add_host(request):
    if request.method == 'POST':
        # save the todo
        form = HostForm(request.POST)
        if form.is_valid():
            todo_text = form.cleaned_data.get('todo_text')
            ToDo.objects.create(todo_text=todo_text)
    
    return redirect('')


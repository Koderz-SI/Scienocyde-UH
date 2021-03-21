from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Host
from django.contrib.auth.models import User
from core.forms import HostForm
from core.forms import ParticipantForm


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
    form = HostForm()
    context = {"app_name": "Scienocyde-UH-1", "form": form}

    return render(request, template_name, context=context)

def add_host(request):
    username = request.user.get_username()
    if request.method == "POST":
        form = HostForm(request.POST)
        if form.is_valid():
            Your_Full_Name = form.cleaned_data.get("Your_Full_Name")
            Email_address = form.cleaned_data.get("Email_address")
            Organization_hosting_the_contest = form.cleaned_data.get(
                "Organization_hosting_the_contest"
            )
            Type_of_Organization = form.cleaned_data.get("Type_of_Organization")
            Designation = form.cleaned_data.get("Designation")
            Phone_no = form.cleaned_data.get("Phone_no")
            Purpose_of_Contest = form.cleaned_data.get("Purpose_of_Contest")
            Breif_detail_about_your_event = form.cleaned_data.get(
                "Breif_detail_about_your_event"
            )
            Theme_of_Project = form.cleaned_data.get("Theme_of_Project")
            Guidelines_for_submission = form.cleaned_data.get(
                "Guidelines_for_submission"
            )
            Eligibility_Creteria = form.cleaned_data.get("Eligibility_Creteria")
            Host.objects.create(
                username=username,
                full_name=Your_Full_Name,
                email=Email_address,
                org=Organization_hosting_the_contest,
                type_org=Type_of_Organization,
                designation=Designation,
                phone=Phone_no,
                purpose=Purpose_of_Contest,
                detail=Breif_detail_about_your_event,
                theme=Theme_of_Project,
                guidelines=Guidelines_for_submission,
                elig_cri=Eligibility_Creteria,
            )

    return redirect("host_dashboard")


def host_dashboard(request):
    username = request.user.get_username()
    host_obj = Host.objects.get(username=username)
    template_name = "core/dashboard.html"
    context = {"host_obj": host_obj, "username": username}
    return render(request, template_name, context)

def applyto(request):
    template_name = "core/applyto.html"
    return render(request, template_name)

def detail(request):
    template_name = "core/detail.html"
    return render(request, template_name)

def participant(request):
    template_name = "core/participant.html"
    form = ParticipantForm()
    context = {"app_name": "Scienocyde-UH-1", "form": form}

    return render(request, template_name, context=context)


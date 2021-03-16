from django import forms

class HostForm(forms.Form):
	Your_Full_Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Full Name'}))
	Email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'name@example.com'}))
	Organization_hosting_the_contest = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	Type_of_Organization = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	Designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	Phone_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':''}))
	Purpose_of_Contest = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':''}))
	Breif_detail_about_your_event = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':''}))
	Theme_of_Project = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	Guidelines_for_submission = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':''}))
	Eligibility_Creteria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	

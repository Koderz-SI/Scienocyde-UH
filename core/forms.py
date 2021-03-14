from django import forms

class HostForm(forms.Form):
	full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Full Name'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'name@example.com'}))
	org = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	type_org = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':''}))
	purpose = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':''}))
	detail = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':''}))
	theme = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	guidelines = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':''}))
	elig_cri = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':''}))
	
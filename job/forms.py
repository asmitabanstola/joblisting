from django import forms
from .models import Job,Category

class JobForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}))
    skills=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Skills'}))
    company_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Company Name'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    location=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Location'}))
    salary=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control','type':'number','placeholder':'Enter Salary'}))
    expire_date=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image=forms.ImageField()

    class Meta:
        model=Job
        fields='__all__'
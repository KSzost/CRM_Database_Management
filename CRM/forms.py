from django import forms
from django.forms import ModelChoiceField
from .models import *


class registerForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'surname', 'login', 'password', 'date_of_birth')

class addUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'surname', 'login', 'password', 'date_of_birth', 'rule')


class editUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'surname', 'login', 'password', 'date_of_birth', 'rule')
        

class addCompanyForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = ('name', 'nip', 'adres', 'city', 'trade')

class editCompanyForm(forms.ModelForm):

    class Meta:
        model = Companies
        fields = ('name', 'nip', 'adres', 'city', 'trade')


class addContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'surname', 'phone', 'mail', 'job', 'company')


class addNoteForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ('content', 'company')



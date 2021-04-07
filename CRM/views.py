from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import *
from .models import *

def index(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.id_deleted = 0
            user.save()
        return redirect(index)
    else:
        form = registerForm()
        return render(request, 'CRM/index.html', {'form': form})


#Podział panelów obsługi firm
def companiesManagement(request):
    companies_list = Companies.objects.filter(id_deleted = 0).order_by('-id')
    template = loader.get_template('CRM/companiesManagement.html')
    context = {'companies_list': companies_list} 
    return render(request, 'CRM/companiesManagement.html', context)

def deletedCompanies(request):
    companies_list = Companies.objects.filter(id_deleted = 1).order_by('-id')
    template = loader.get_template('CRM/companiesManagement.html')
    context = {'companies_list': companies_list} 
    return render(request, 'CRM/companiesManagement.html', context)

def activeCompanies(request):
    companies_list = Companies.objects.filter(id_deleted = 0).order_by('-id')
    template = loader.get_template('CRM/companiesManagement.html')
    context = {'companies_list': companies_list} 
    return render(request, 'CRM/companiesManagement.html', context)

def allCompanies(request):
    companies_list = Companies.objects.order_by('-id')
    template = loader.get_template('CRM/companiesManagement.html')
    context = {'companies_list': companies_list} 
    return render(request, 'CRM/companiesManagement.html', context)

def deleteCompany(request, company_id):
    company = get_object_or_404(Companies, pk=company_id)
    company.id_deleted = 1
    company.save()
    return redirect(activeCompanies)

def companyAddPanel(request):
    if request.method == "POST":
        form = addCompanyForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(Users, pk=1)
            company = form.save(commit=False)
            company.id_deleted = 0
            company.user = user
            company.save()
        return redirect(activeCompanies)
    else:
        form = addCompanyForm()
        return render(request, 'CRM/addForm.html', {'form': form})

def companyEditPanel(request, company_id):
    if request.method == "POST":
        form = addCompanyForm(request.POST)
        if form.is_valid():
            companydeleted = get_object_or_404(Companies, pk=company_id)
            user = get_object_or_404(Users, pk=1)
            company = form.save(commit=False)
            company.id_deleted = companydeleted.id_deleted
            company.user = companydeleted.user
            companydeleted.delete()
            company.save()
        return redirect(activeCompanies)
    else:
        company = get_object_or_404(Companies, pk=company_id)
        form = addCompanyForm(instance = company)
        return render(request, 'CRM/addForm.html', {'form': form})


#Podział panelów obsługi kontaktów
def contactManagement(request):
    contact_list = Contact.objects.filter(id_deleted = 0).order_by('-id')
    template = loader.get_template('CRM/contactManagement.html')
    context = {'contact_list': contact_list} 
    return render(request, 'CRM/contactManagement.html', context)

def deletedContacts(request):
    contact_list = Contact.objects.filter(id_deleted = 1).order_by('-id')
    template = loader.get_template('CRM/contactManagement.html')
    context = {'contact_list': contact_list} 
    return render(request, 'CRM/contactManagement.html', context)

def activeContacts(request):
    contact_list = Contact.objects.filter(id_deleted = 0).order_by('-id')
    template = loader.get_template('CRM/contactManagement.html')
    context = {'contact_list': contact_list} 
    return render(request, 'CRM/contactManagement.html', context)

def allContacts(request):
    contact_list = Contact.objects.order_by('-id')
    template = loader.get_template('CRM/contactManagement.html')
    context = {'contact_list': contact_list} 
    return render(request, 'CRM/contactManagement.html', context)

def deleteContact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.id_deleted = 1
    contact.save()
    return redirect(activeContacts)

def contactAddPanel(request):
    template = loader.get_template('CRM/contactManagement.html')
    if request.method == "POST":
        form = addContactForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(Users, pk=1)
            contact = form.save(commit=False)
            contact.id_deleted = 0
            contact.user = user
            contact.save()
        return redirect(activeContacts)
    else:
        form = addContactForm()
        return render(request, 'CRM/addForm.html', {'form': form})

def contactEditPanel(request, contact_id):
    template = loader.get_template('CRM/contactManagement.html')
    if request.method == "POST":
        form = addContactForm(request.POST)
        if form.is_valid():
            contactdeleted = get_object_or_404(Contact, pk=contact_id)
            contact = form.save(commit=False)
            contact.id_deleted = contactdeleted.id_deleted
            contact.user = contactdeleted.user
            contact.save()
            contactdeleted.delete()
        return redirect(activeContacts)
    else:
        contact = get_object_or_404(Contact, pk=contact_id)
        form = addContactForm(instance = contact)
        return render(request, 'CRM/addForm.html', {'form': form})


#Podział panelów obsługi notatek
def notesManagement(request):
    notes_list = Notes.objects.filter(id_deleted = 0).order_by('-id')
    template = loader.get_template('CRM/notesManagement.html')
    context = {'notes_list': notes_list} 
    return render(request, 'CRM/notesManagement.html', context)

def deletedNotes(request):
    notes_list = Notes.objects.filter(id_deleted = 1).order_by('-id')
    template = loader.get_template('CRM/notesManagement.html')
    context = {'notes_list': notes_list} 
    return render(request, 'CRM/notesManagement.html', context)

def activeNotes(request):
    notes_list = Notes.objects.filter(id_deleted = 0).order_by('-id')
    template = loader.get_template('CRM/notesManagement.html')
    context = {'notes_list': notes_list} 
    return render(request, 'CRM/notesManagement.html', context)

def allNotes(request):
    notes_list = Notes.objects.order_by('-id')
    template = loader.get_template('CRM/notesManagement.html')
    context = {'notes_list': notes_list} 
    return render(request, 'CRM/notesManagement.html', context)

def deleteNote(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    note.id_deleted = 1
    note.save()
    return redirect(activeNotes)

def noteAddPanel(request):
    if request.method == "POST":
        form = addNoteForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(Users, pk=1)
            note = form.save(commit=False)
            note.id_deleted = 0
            note.user = user
            note.save()
        return redirect(activeNotes)
    else:
        form = addNoteForm()
        return render(request, 'CRM/addForm.html', {'form': form})

def noteEditPanel(request, note_id):
    if request.method == "POST":
        form = addNoteForm(request.POST)
        if form.is_valid():
            notedeleted = get_object_or_404(Notes, pk=note_id)
            note = form.save(commit=False)
            note.id_deleted = notedeleted.id_deleted
            note.user = notedeleted.user
            notedeleted.delete()
            note.save()
        return redirect(activeNotes)
    else:
        note = get_object_or_404(Notes, pk=note_id)
        form = addNoteForm(instance = note)
        return render(request, 'CRM/addForm.html', {'form': form})


#Podział panelów obsługi branż
def tradesManagement(request):
    trades_list = Trades.objects.order_by('-id')
    template = loader.get_template('CRM/tradesManagement.html')
    context = {'trades_list': trades_list} 
    return render(request, 'CRM/tradesManagement.html', context)


#Podział panelów obsługi ról
def rulesManagement(request):
    rules_list = Rules.objects.order_by('-id')
    template = loader.get_template('CRM/rulesManagement.html')
    context = {'rules_list': rules_list} 
    return render(request, 'CRM/rulesManagement.html', context)

#Podział panelów obsługi userów
def usersManagement(request):
    users_list = Users.objects.filter(id_deleted = 0).order_by('-id')
    template = loader.get_template('CRM/usersManagement.html')
    context = {'users_list': users_list} 
    return render(request, 'CRM/usersManagement.html', context)

def deletedUsers(request):
    users_list = Users.objects.filter(id_deleted = 1).order_by('-id')
    template = loader.get_template('CRM/usersManagement.html')
    context = {'users_list': users_list} 
    return render(request, 'CRM/usersManagement.html', context)

def activeUsers(request):
    users_list = Users.objects.filter(id_deleted = 0).order_by('-id')
    template = loader.get_template('CRM/usersManagement.html')
    context = {'users_list': users_list} 
    return render(request, 'CRM/usersManagement.html', context)

def allUsers(request):
    users_list = Users.objects.order_by('-id')
    template = loader.get_template('CRM/usersManagement.html')
    context = {'users_list': users_list} 
    return render(request, 'CRM/usersManagement.html', context)

def deleteUser(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    user.id_deleted = 1
    user.save()
    return redirect(activeUsers)

def userAddPanel(request):
    if request.method == "POST":
        form = addUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.id_deleted = 0
            user.save()
        return redirect(activeUsers)
    else:
        form = addUserForm()
        return render(request, 'CRM/addForm.html', {'form': form})

def userEditPanel(request, user_id):
    if request.method == "POST":
        form = editUserForm(request.POST)
        if form.is_valid():
            userdeleted = get_object_or_404(Users, pk=user_id)
            user = form.save(commit=False)
            user.id_deleted = userdeleted.id_deleted
            userdeleted.delete()
            user.save()
        return redirect(activeUsers)
    else:
        user = get_object_or_404(Users, pk=user_id)
        form = editUserForm(instance=user)
        return render(request, 'CRM/editUser.html', {'form': form})


    



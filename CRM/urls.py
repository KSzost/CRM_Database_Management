from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('index.html', views.index, name='index'),

    #widoki zarządzania użytkownikami
    path('usersManagement', views.usersManagement, name='usersManagement'),
    path('deletedUsers', views.deletedUsers),
    path('allUsers', views.allUsers),
    path('activeUsers', views.activeUsers),
    path('deleteUser/<int:user_id>/', views.deleteUser, name='deleteUser'),
    path('userAddPanel', views.userAddPanel),
    path('userEditPanel/<int:user_id>/', views.userEditPanel, name='userEditPanel'),

    #widoki zarządzania firmami
    path('companiesManagement', views.companiesManagement, name='companiesManagement'),
    path('deletedCompanies', views.deletedCompanies),
    path('allCompanies', views.allCompanies),
    path('activeCompanies', views.activeCompanies),
    path('deleteCompany/<int:company_id>/', views.deleteCompany, name='deleteCompany'),
    path('companyAddPanel', views.companyAddPanel),
    path('companyEditPanel/<int:company_id>/', views.companyEditPanel, name='companyEditPanel'),

    #widoki zarządzania kontaktami
    path('contactManagement', views.contactManagement, name='contactManagement'),
    path('deletedContacts', views.deletedContacts),
    path('allContacts', views.allContacts),
    path('activeContacts', views.activeContacts),
    path('deleteContact/<int:contact_id>/', views.deleteContact, name='deleteContact'),
    path('contactEditPanel/<int:contact_id>/', views.contactEditPanel, name='contactEditPanel'),
    path('contactAddPanel', views.contactAddPanel),

    #widoki zarządzania notatkami
    path('notesManagement', views.notesManagement, name='notesManagement'),
    path('deletedNotes', views.deletedNotes),
    path('allNotes', views.allNotes),
    path('activeNotes', views.activeNotes),
    path('deleteNote/<int:note_id>/', views.deleteNote, name='deleteNote'),
    path('noteAddPanel', views.noteAddPanel),
    path('noteEditPanel/<int:note_id>/', views.noteEditPanel, name='noteEditPanel'),

    #widoki zarządzania branżami
    path('tradesManagement', views.tradesManagement, name='tradesManagement'),

    #widoki zarządzania rolami
    path('rulesManagement', views.rulesManagement, name='rulesManagement'),

    
]

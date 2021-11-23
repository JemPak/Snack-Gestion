"""Gestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.Installation import views as install
from apps.Contact import views as contact

urlpatterns = [
    path('contact/', contact.ContactListCreateView.as_view()),                            #create a new contact request
    path('contact/<int:pk>', contact.ContactRetrieveUpdateDestroy.as_view()),             #retrieve a request with the pk   
    path('contact/active', contact.contactView.ContactIsActiveView.as_view()),            #retrive all the request that is active  
    path('contact/user/<int:user_id>/<str:active>', contact.contactView.ContactUser.as_view()),       #list contacts by user id    
    path('installation/', install.InstallationListCreateView.as_view()),                  #create a new installation request 
    path('installation/<int:pk>', install.InstallationRetrieveUpdateDestroy.as_view()),   #retrieve a request with the pk
    path('installation/unaccepted', install.installationView.InstallationIsAcceptedView.as_view()),  
    path('installation/user/<int:user_id>/<str:active>', install.installationView.InstallationUser.as_view()), #retrieve user installations active or inactive
]

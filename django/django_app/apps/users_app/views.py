from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'Placeholder to later display all the list of users'
    return HttpResponse(response)

def new(request):
    response = 'Placeholder to later create new user records'
    return HttpResponse(response)

def register(request):
    response = 'Placeholder for users to create a new user record'
    return HttpResponse(response)

def login(request):
    response = 'Placeholder for users to login'
    return HttpResponse(response)
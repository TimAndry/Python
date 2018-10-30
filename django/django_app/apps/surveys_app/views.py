from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'Placeholder to later display all the list of surveys'
    return HttpResponse(response)

def new(request):
    response = 'Placeholder for users to create a new survey'
    return HttpResponse(response)
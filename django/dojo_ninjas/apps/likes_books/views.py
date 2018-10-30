from django.shortcuts import render, HttpResponse

def index(request):
    response = "new page works"
    return HttpResponse(response)
# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):
    time = {
        "time": strftime(" %H:%M %p on %b %d, %Y", localtime())
    }
    return render(request, 'time_app/index.html', time)

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from django import forms
def index(request):
    
    return render(request, 'survey_app/index.html')


def page(request):
    if request.method == 'POST':
        if 'count' in request.session:
            request.session['count'] +=1
        else:
            request.session['count'] = 1
        request.session['name'] = request.POST['name']
        request.session['email'] = request.POST['email']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['message'] = request.POST['message']
        print(request.session['location'], request.session['language'])
    return redirect('/results')


def results(request):

    return render(request, 'survey_app/results.html')
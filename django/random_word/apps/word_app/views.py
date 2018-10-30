from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' in request.session:
        request.session['count'] = request.session['count']
    else:
        request.session['count'] = 0
    return render(request, 'word_app/index.html')

def generate(request):
    request.session['count'] = request.session['count'] + 1
    request.session['dna'] = get_random_string(length = 16, allowed_chars='ACTG')
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
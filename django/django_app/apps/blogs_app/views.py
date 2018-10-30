from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'Placeholder to later display all the list of blogs'
    return HttpResponse(response)

def new(request):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    response = 'placeholder to display blog number ' + number
    print(number)
    return HttpResponse(response)

def edit(request, number):
    response = 'placeholder to edit blog number ' + number
    print(number)
    return HttpResponse(response)

def delete(request, number):
    response = 'placeholder to delete blog number ' + number
    print(number)
    return HttpResponse(response)


def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"  # more on session below
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")

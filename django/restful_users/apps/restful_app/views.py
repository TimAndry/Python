from django.shortcuts import render, redirect
from .models import *

def index(request):
    user = User.objects.all()
    context = {
        'users':user,
        #'email':users_table,
    }
    print(user)
    return render(request, "restful_app/index.html", context, user)

def new(request):
    return render(request, "restful_app/new.html")

def create(request):
    new_user = User.objects.create(name = request.POST['first_name'] + ' ' + request.POST['last_name'], email = request.POST['email'])
    return redirect('/')

def show(request, user_id):
    this_user = User.objects.get(id=user_id)
    print(this_user.name)
    context = {
       'user': this_user 
    }
    return render(request, 'restful_app/show.html', context)

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    print(user.name)
    context = {
        'user': user
    }

    return render(request, 'restful_app/edit.html', context)

def update(request, user_id):
    if request.method == 'POST':
        update = User.objects.get(id=user_id)
        update.name = request.POST['fname'] + " " + request.POST['lname']
        update.email = request.POST['email']
        update.save()
        user_id = str(update.id)
        return redirect('/show/' + user_id)

def delete(request, user_id):
    delete = User.objects.get(id=user_id)
    delete.delete()
    return redirect('/')
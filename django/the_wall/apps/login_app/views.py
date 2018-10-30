from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import re, bcrypt, datetime

"""

A SHORT LIST OF REGULAR EXPRESSIONS
^                  // the start of the string
(?=.*[a-z])        // use positive look ahead to see if at least one lower case letter exists
(?=.*[A-Z])        // use positive look ahead to see if at least one upper case letter exists
(?=.*\d)           // use positive look ahead to see if at least one digit exists
(?=.*[_\W])        // use positive look ahead to see if at least one underscore or non-word character exists
.+                 // gobble up the entire string
$                  // the end of the string

"""



#use regualr expression to validate email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#looks for one number
NAME_REGEX = re.compile(r'[0-9]')
#looks for one lower case, one upper case, and one number
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)')

def index(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        context = {
            'user':user
        }
    else:
        context = {}
    return render(request, 'login_app/index.html', context)

def registration(request):
    result = User.objects.validate_registration(request.POST)
    if len(result) > 0:
        for key in result.keys():
            print(result[key])
            messages.error(request, result[key], extra_tags = key)
    else:
        #hash the password
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], password = hashed_pw, email = request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('user/' + str(request.session['user_id']))
    return redirect('/')

def login(request):
    user = User.objects.filter(email = request.POST['em2ail'])
    if len(user) == 0:
        messages.error(request, 'This user does not exist', extra_tags = 'em2ail')
        return redirect('/')
    else:
        user = user.first()
    #Checks if passwords are valid .checkpw
    valid_pass = bcrypt.checkpw(request.POST['pass2word'].encode(), user.password.encode())
    if request.POST['pass2word'] == "":
        messages.error( request, 'enter a valid password', extra_tags = 'pass2word')
    if valid_pass:
        request.session['user_id'] = user.id
        messages.error( request, user.first_name + ' is now logged in', extra_tags = 'em2ail')
        print(user.first_name)
        return redirect('user/' + str(request.session['user_id']))
    else:
        messages.error( request, 'Password email combination not found', extra_tags = 'em2ail')
    return redirect('/')


def user(request, user_id):
    user = User.objects.get(id = request.session['user_id'])
    message = Message.objects.all()
    comment = Comment.objects.all()
    context = {
        'message': message,
        'user': user,
        'comment': comment,
    }
    return render(request, 'login_app/user.html', context)

def wall(request):
    user = User.objects.get(id = request.session['user_id'])
    print(user)
    message = Message.objects.all()
    comment = Comment.objects.all()
    context = {
        'message': message,
        'user': user,
        'comment': comment,
    }
    return render(request, 'login_app/wall.html', context)

def message(request):
    Message.objects.create(message = request.POST['message'], user_id = request.session['user_id'])
    
    return redirect('/wall')

def comment(request):
    Comment.objects.create(comment = request.POST['comment'], message_id = request.POST['message_id'], user_id = request.session['user_id'])

    return redirect('/wall')

def delete(request):
    message = Message.objects.get(id = request.POST['delete_button'])
    if message.user_id == request.session['user_id']:
        message.delete()
        return redirect('/wall')
    else:
        messages.error(request, 'You can only delete your own post', extra_tags = 'delete_button')
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')

def tables(request):
    user = User.objects.all().order_by('-id')
    message = Message.objects.all()
    comment = Comment.objects.all()
    context = {
        'user': user,
        'message': message,
        'comment': comment,
    }
    return render(request, 'login_app/tables.html', context)
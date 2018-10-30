from django.shortcuts import render, redirect
#used to import messages
from django.contrib import messages
from .models import *
import re, bcrypt


# A SHORT LIST OF REGULAR EXPRESSIONS
# ^                  // the start of the string
# (?=.*[a-z])        // use positive look ahead to see if at least one lower case letter exists
# (?=.*[A-Z])        // use positive look ahead to see if at least one upper case letter exists
# (?=.*\d)           // use positive look ahead to see if at least one digit exists
# (?=.*[_\W])        // use positive look ahead to see if at least one underscore or non-word character exists
# .+                 // gobble up the entire string
# $                  // the end of the string



#use regualr expression to validate email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#looks for one number
NAME_REGEX = re.compile(r'[0-9]')
#looks for one lower case, one upper case, and one number
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)')

def index(request):
    if 'user_id' not in request.session:
         return render(request, 'login_app/index.html')    
    user = User.objects.get(id = request.session['user_id'])
    context = {
        'user':user
    }
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
        messages.error( request, 'This password email combination was not found', extra_tags = 'em2ail')
    return redirect('/')


def user(request, user_id):
    if 'user_id' not in request.session:
        return render(request, 'login_app/error.html')
    user = User.objects.get(id = request.session['user_id'])
    liked_quote = user.liked_quotes.all()
    print(liked_quote)
    quote = Quote.objects.all()
    context = {
        'user':user,
        'quote':quote,
        'liked_quote': liked_quote,
    }
    return render(request, 'login_app/user.html', context)

def quote(request):
    result = User.objects.validate_quote(request.POST)
    if len(result) > 0:
        for key in result.keys():
            print(result[key])
            messages.error(request, result[key], extra_tags = key)
        return redirect('user/' + str(request.session['user_id']))
    else:
        Quote.objects.create(author = request.POST['author'], this_quote = request.POST['quote'], quoter_id = request.session['user_id'])
        return redirect('user/' + str(request.session['user_id']))

def q2uote(request):
    result = User.objects.validate_quote(request.POST)
    if len(result) > 0:
        for key in result.keys():
            print(result[key])
            messages.error(request, result[key], extra_tags = key)
        return redirect('/full')
    else:
        Quote.objects.create(author = request.POST['author'], this_quote = request.POST['quote'], quoter_id = request.session['user_id'])
        return redirect('/full')


def edit(request, user_id):
    if 'user_id' not in request.session:
        return render(request, 'login_app/error.html')
    user = User.objects.get(id = request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'login_app/edit.html', context)

def update(request, user_id):
    result = User.objects.validate_edit(request.POST)
    if len(result) > 0:
        for key in result.keys():
            print(result[key])
            messages.error(request, result[key], extra_tags = key)
        return redirect('/edit/' + str(request.session['user_id']))
    else:
        #hash the password
        #hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.get(id = request.session['user_id'])
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        #user.password = request.POST['password']
        user.save()
        
        return redirect('/user/' + str(request.session['user_id']))

def delete(request):
    quote = Quote.objects.get(id = request.POST['delete_button'])
    if quote.quoter_id == request.session['user_id']:
        quote.delete()
        return redirect('/user/' + str(request.session['user_id']))
    else:
        messages.error(request, 'You can only delete your own post', extra_tags = 'delete_button')
    return redirect('/user/' + str(request.session['user_id']))

def del2ete(request):
    quote = Quote.objects.get(id = request.POST['delete_button'])
    if quote.quoter_id == request.session['user_id']:
        quote.delete()
        return redirect('/full')
    else:
        messages.error(request, 'You can only delete your own post', extra_tags = 'delete_button')
    return redirect('/full')

def full(request):
    if 'user_id' not in request.session:
        quote = Quote.objects.all()
        context = {
            'quote': quote
        }
        return render(request, 'login_app/full.html', context)
    user = User.objects.get(id = request.session['user_id'])
    quote = Quote.objects.all()
    context = {
        'user':user,
        'quote':quote,
    }
    return render(request, 'login_app/full.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')


def added(request, quote_quoter_id):
    user = User.objects.get(id = quote_quoter_id)
    quote = Quote.objects.filter(quoter_id = quote_quoter_id)
    context = {
        'quote':quote,
        'user':user,
    }
    return render(request, 'login_app/added.html', context)


def like(request):
    liked_users = User.objects.get(id = request.POST['user'])
    liked_quotes = Quote.objects.get(id = request.POST['quote'])
    liked_users.liked_quotes.add(liked_quotes)
    print(liked_quotes.liked_users.count())
    return redirect('/full')

def error(request):
    return render(request, 'login_app/error.html')
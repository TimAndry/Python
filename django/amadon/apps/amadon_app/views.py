from django.shortcuts import render, redirect
from .models import *

def index(request):
    items = Item.objects.all()
    context = {
        'item': items
    }
    if 'total_items' not in request.session:
        request.session['total_items'] = 0
        request.session['total_spent'] = 0
    else:
        request.session['total_items'] = request.session['total_items']
        request.session['total_spent'] = request.session['total_spent']
    return render(request, 'amadon_app/index.html', context, items)

def total(request):
    if request.method == 'POST':
        this_item = request.POST['it_em']
        this_number = request.POST['number']
        request.session['total_number'] = this_number
        this_price = Item.objects.get(id=this_item).price
        total_price = float(this_price) * int(this_number)
        request.session['total_price'] = total_price
        request.session['id'] = Item.objects.get(id=this_item).id
        request.session['total_items'] = int(request.session['total_items']) + int(request.session['total_number'])
        request.session['total_spent'] = request.session['total_spent'] + request.session['total_price']
    return redirect('/confirmation')


def confirmation(request):
    name = Item.objects.get(id=request.session['id']).name
    print(name)
    context = {
        'name': name
    }
    return render(request, 'amadon_app/confirmation.html', context)
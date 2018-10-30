from django.shortcuts import render, redirect
from random import randint
from time import gmtime, strftime, localtime
  
def index(request):
    if 'total_gold' in request.session:
        request.session['total_gold'] = request.session['total_gold']
        if request.session['total_gold'] >= 200:
            request.session['image'] = 'goldenshower.gif'
        else:
            request.session['image'] = 'golden_ninja.gif'
    else:
        request.session['total_gold'] = 100
        request.session['image'] = 'golden_ninja.gif'
    if 'place' in request.session:
        request.session['place'] = request.session['place']
    else:
        request.session['place'] = 'outta nowhere'
    if 'earned_gold' in request.session:
        request.session['earned_gold'] = request.session['earned_gold']
    else:
        request.session['earned.gold'] = 0
    if 'display_result' not in request.session:
        request.session['display_result'] = []
    return render(request, 'gold_app/index.html')

def process(request):
    if request.method == 'POST':
        if 'farmgold' in request.POST:
            request.session['earned_gold'] =  randint(10, 20)
            print(request.session['earned_gold'])
            request.session['place'] = 'farm'
            request.session['total_gold'] = request.session['total_gold'] + request.session['earned_gold']
        if 'cavegold' in request.POST:
            request.session['earned_gold'] =  randint(5, 10)
            print(request.session['earned_gold'])
            request.session['place'] = 'cave'
            request.session['total_gold'] += request.session['earned_gold']
        if 'housegold' in request.POST:
            request.session['earned_gold'] =  randint(2, 5)
            print(request.session['earned_gold'])
            request.session['place'] = 'house'
            request.session['total_gold'] += request.session['earned_gold']
        if 'casinogold' in request.POST:
            request.session['place'] = 'casino'
            doordie = randint(1,2)
            if doordie == 1:    
                request.session['earned_gold'] = randint(1,50)
                print(request.session['earned_gold'])
            elif doordie == 2:
                request.session['earned_gold'] = randint(1,50) * -1
            request.session['total_gold'] += request.session['earned_gold']

        time = strftime(" %H:%M %p on %b %d, %Y", localtime())
        

        if request.session['earned_gold'] > 0: 
            request.session['result'] = '<span class="green"><p>Congratulations!! You earned ' + str(request.session['earned_gold']) + ' gold from the ' + request.session['place'] +' at...             ' + str(time) + '</p></span>'

        elif request.session['earned_gold'] < 0:
            request.session['result'] = '<span class="red"><p>OH NO! Your greed lost you ' + str(request.session['earned_gold']) + ' gold from the ' + request.session['place'] +' at...             ' + str(time) + '</p></span>'

        temp_result = request.session['display_result']
        temp_result.append(request.session['result'])
        request.session['display_result'] = temp_result
        
    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')

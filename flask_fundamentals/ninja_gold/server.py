from flask import Flask, render_template, url_for, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

from random import randint
import time, calendar

count = 0
resultlist = list()
image = 'golden_ninja.gif'

@app.route('/')
def index():
    if 'time' in session:
        ts = time.gmtime()
        session['time'] = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    else:
        session['time'] = time.gmtime()
    #assign arbitrary place to session if none is found
    if 'place' in session:
        session['place'] = session['place']
    else:
        session['place'] = 'outta nowhere'
    #checks for total gold and resets its value if not found in session
    if 'totalgold' in session:
        session['totalgold'] = session['totalgold']
        if session['totalgold'] >= 200:
            image = 'goldenshower.gif'
        else:
            image = 'golden_ninja.gif'
    else:
        session['totalgold'] = 100
        image = 'golden_ninja.gif'
    #changes the list into a string
    showresult = " ".join(resultlist)

    #added count functionality to count number of guess attempts
    if 'count' in session:
        session['count'] = session['count']
    else:
        session['count'] = 0 

    #returns values to session and index.html
    return render_template('index.html', total = session['totalgold'], activity_results = showresult, total_gold = session['totalgold'], count = session['count'], image = image, )



@app.route('/process_money', methods=['POST'])
def money():
    #gets gold from farm action and changes the place to farm
    if 'farmgold' in request.form:
        session['earnedgold'] = randint(10, 20)
        session['place'] = 'farm'
        session['totalgold'] = session['totalgold'] - 12
        session['count'] = session['count'] + 1

    #gets gold from cave action and changes the place to cave   
    elif 'cavegold' in request.form:
        session['earnedgold'] = randint(5, 10)
        session['place'] = 'cave'
        session['totalgold'] = session['totalgold'] - 7
        session['count'] = session['count'] + 1

    #gets gold from house action and changes the place to house    
    elif 'housegold' in request.form:
        session['earnedgold'] = randint(2, 5)
        session['place'] = 'house'
        session['totalgold'] = session['totalgold'] - 3
        session['count'] = session['count'] + 1
        
    #gets gold from casino action and changes the place to casino
    elif 'casinogold' in request.form:
        session['place'] = 'casino'
        winlose = randint(1,2)
        print(winlose)
        if winlose == 1: #wins money
            session['earnedgold'] = randint(1, 50)
        elif winlose == 2: #loses money
            session['earnedgold'] = randint(1, 50) * -1
        session['totalgold'] = session['totalgold'] - 1
        session['count'] = session['count'] + 1

    #adds total gold to earned gold and stores it in the session
    
    if session['earnedgold'] > 0 and session['totalgold'] < 200:#makes text green
        result = '<span class="green"><p>Congratulations!! You earned ' + str(session['earnedgold']) + ' gold from the ' + session['place'] +' at...             ' + str(session['time']) + '</p></span>'

    elif session['earnedgold'] < 0 and session['totalgold'] < 200: #makes text red
        result = '<span class="red"><p>OH NO! Your greed lost you ' + str(session['earnedgold']) + ' gold from the ' + session['place'] +' at...             ' + str(session['time']) + '</p></span>'

    #edge case if gold earned is 0 nothing will return
    elif session['earnedgold'] == 0:
        result = ''

    session['totalgold'] = session['totalgold'] + session['earnedgold']

    print(session['totalgold'])

    #appends results of logic statements to the list to be displayed in the activities div
    resultlist.append(result)
    return redirect('/')


@app.route('/reset', methods=['post']) 
def startOver():
    session.clear()

    #clears the session
    resultlist.clear()

    #clears the list of actions
    print(resultlist)

    #sets count to 0
    count = 0
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

    
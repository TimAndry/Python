from flask import Flask, render_template, url_for, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

from random import randint


@app.route('/')
def index():
    value = 'text'
    value2 = ''
    if 'count' in session:
        session['count'] = session['count']
    else:
        session['count'] = 0 
    #added count functionality to count number of guess attempts
    if 'number' in session:
        ninja_image = 'runninja.gif'
    else:
        session['number'] = randint(1, 101)
        ninja_image = 'runninja.gif'
    print(session['number'])
    if 'guess' in session:
        print(session['guess'])
    else:
        session['guess'] = 0
    if session['guess'] < session['number'] and session['guess'] > 0:
        ninja_image = 'upper.gif'
        return render_template('index.html', image = ninja_image, value = value, value2 = value2, count = session['count'])
    if session['guess'] > session['number']:
        ninja_image = 'down.gif'
        return render_template('index.html', image = ninja_image, value = value, value2 = value2, count = session['count'])
    if session['guess'] == 0 or session['guess'] == "":
        ninja_image = 'runninja.gif'
        return render_template('index.html', image = ninja_image, value = value, value2 = value2, count = session['count'])
    if session['guess'] == session['number']:
        value = 'hidden'
        value2 = 'display: none;'
        winner = 'CONGRATULATIONS!!!' + '<br>' + 'You guesed my number in ' + str(session['count']) + ' tries!!'
        print('correct')
        ninja_image = 'correctninja.gif'
        #session.clear()
        return render_template('index.html', image = ninja_image, value = value, value2 = value2, congrats = winner, count = session['count'])
        #after guess is correct, session is cleared and everything is returned except the session number
    return render_template('index.html', image = ninja_image, num= session['number'], value = value, value2 = value2, count = session['count'])

@app.route('/pick_num', methods=['GET'])
def guessRight():
    session['count']+=1
    try:
        session['guess'] = int(request.args.get('guess', False))
        #had to use request.ARGS instead of request.FORM. form arguments were never posted so code always returned false.
    except ValueError:
        print("try again")
        #added validation for if the input cannot be converted into an integer
    return redirect('/')

@app.route('/startover', methods=['GET']) 
def startOver():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
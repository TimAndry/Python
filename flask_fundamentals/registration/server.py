from flask import Flask, render_template, request, redirect, session, flash

#used to perform regular expressions
import re

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
NAME_REGEX = re.compile(r'[0-9]')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


#this is where the form information is posted
@app.route('/page', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    session['password1'] = request.form['password1']
    session['password2'] = request.form['password2']
    message = None
    if len(request.form['email']) < 1:
        message = "Email cannot be blank"
        flash(message) 
    if not EMAIL_REGEX.match(request.form['email']):
        message = "Invalid Email"
        flash(message)
    if len(request.form['fname']) < 2 or NAME_REGEX.search(request.form['fname']):
        message = "please enter valid first name (must be longer than 1 character and contain no numbers)"
        flash(message)
    if len(request.form['fname']) < 2 or NAME_REGEX.search(request.form['lname']):
        message = "please enter valid last name (must be longer than 1 character and contain no numbers)"
        flash(message)
    if len(request.form['password1']) < 8:
        message = "password must be longer than 8 characters"
        flash(message)
    if not PASSWORD_REGEX.match(request.form['email']):
        message = "password must contain 1 number and 1 UPPERCASE letter"
        flash(message)
    if request.form['password1'] != request.form['password2']:
        message = "passwords must match"
        flash(message)
    if session['fname'] != None or session['lname'] != None or session['email'] != None or session['password1'] != None or session['password2'] != None:
        return render_template("index.html", message = message, fname = session['fname'], lname = session['lname'])
    else:
        return redirect('/result')
    return redirect('/')


@app.route('/result', methods=['GET'])
def renderResults():
    #session.clear()
        #if all the information correct and form is submitted the submission redirects to the confirmation page
    message = "Thank you!"
    flash(message)
    return render_template('index.html', message=message)


@app.route('/reset', methods=['POST'])
def resetForm():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
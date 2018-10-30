from flask import Flask, render_template, request, redirect, session, flash

#used to perform regular expressions
import re

#use regualr expression to validate email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['message'] = request.form['message']
    message1 = ""
    message2 = ""
    message3 = ""
    message4 = ""
    comment = session['message']
    if len(request.form['email']) < 1:
        message1 = "Email cannot be blank"
        flash(message1) 
    if not EMAIL_REGEX.match(request.form['email']):
        message2 = "Invalid Email Address"
        flash(message2)
    if len(request.form['name']) < 2:
        message3 = "please enter you full name (must be longer than 1 character)"
        flash(message3)
    if len(request.form['message']) > 120:
        message4 = "message must be less than 140 characters"
        flash(message4)
    if message1 != "" or message2 != "" or message3 != "" or message4 != "":
        return render_template("index.html", message1=message1, message2=message2, message3=message3, message4=message4, comment=comment)
    else:
        #if all the information correct and form is submitted the submission redirects to the confirmation page
        flash("Success!")
        return redirect('/result')
    return redirect('/')


@app.route('/result', methods=['GET'])
def renderResults():
    return render_template('result.html')


@app.route('/reset', methods=['POST'])
def resetForm():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
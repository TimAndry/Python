from flask import Flask, render_template, request, redirect, session, flash
# import the function connectToMySQL from the file mysqlconnection.py

from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('friendsdb')
# now, we may invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM friends WHERE first_name LIKE 'Toussaint';"))


@app.route('/')
def index():
    #search_info = request.form['friend']
    if 'search' not in session:
        session['search'] = ""
    print("got a list of all my friends")
    return render_template('index.html')

@app.route('/page', methods=['POST'])
def search():
    session['search'] = request.form['friend']
    all_friends = mysql.query_db("SELECT * FROM friends WHERE first_name LIKE" + ' "' + session['search'] + '" ' + "OR last_name LIKE" + ' "' + session['search'] + '"')
    tableKey = ['First', 'Last', 'Occupation']
    firstName = []
    lastName = []
    occupation = []
    for i in range(0, len(all_friends)):
        firstName.append(all_friends[i]['first_name'])
    print(firstName)
    for i in range(0, len(all_friends)):
        lastName.append(all_friends[i]['last_name'])
    print(lastName)
    for i in range(0, len(all_friends)):
        occupation.append(all_friends[i]['occupation'])
    print(occupation)
    session['fname'] = firstName
    session['lname'] = lastName
    session['occupation'] = occupation
    session['keys'] = tableKey
    return redirect('/result')

@app.route('/database', methods=['POST'])
def addfriend():
    fname = request.form['fname']
    lname = request.form['lname']
    occupation = request.form['occupation']
    mysql.query_db("INSERT INTO friends (first_name, last_name, occupation) VALUES (" + '"'+ fname +'"'+',' + '"'+lname + '"'+',' + '"'+occupation + '"'+');')
    session['message'] = 'successfully added a name!'
    return redirect('/addition')

@app.route('/addition', methods=['GET'])
def messages():
    message = session['message']
    return render_template('index.html', message = message)

@app.route('/result')
def showfriend():
    firstName = session['fname']
    lastName = session['lname']
    occupation = session['occupation']
    tableKey = session['keys']
    return render_template('index.html', fname = firstName, lname = lastName, occupation = occupation, keys = tableKey)  

if __name__ == "__main__":
    app.run(debug=True)

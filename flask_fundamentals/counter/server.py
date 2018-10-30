from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

app.count = 0

@app.route('/')
def index(): 
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1 
    return render_template("index.html", count = session['count'])


@app.route('/result', methods=['GET'])
def add1():
    session['count'] += 1
    print(session['count'])
    return redirect('/')


@app.route('/clear', methods=['GET'])
def clearall():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)
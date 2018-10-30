from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    print('hello world')#on the terminal
    return '<h1>hello world</h1>'#on the html page

@app.route('/dojo')
def dojopage():
    print('dojo')
    return '<h1>Coding Dojo</h1>'

@app.route('/say/<name>')
def say(name):#takes in a variable name and passes it to the <name> route of the address
    print(name)
    return "<h1>hello "+name+ "</h1>" 

@app.route('/repeat/<num>/<word>') #takes two variables and passes them as routes to the address
def repeat(num, word):
    print(num)
    print(word)
    
    return ('<p>'+word+'\n'+'</p>')*int(num) + num




"""@app.route('/say/michael')
say():
    print('name')
    return '<h1>Hi Michael</h1>'

@app.route('/say/john')
say():
    print('name')
    return '<h1>Hi John</h1>'"""


if __name__=="__main__":

    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    redblock = "<div id='red'></div>"
    blackblock = "<div id='black'></div>"
    redblock2 = "<div id='red'></div>"
    blackblock2 = "<div id='black'></div>"
    row = blackblock
    row2 = redblock
    for i in range(0,3):
        row = row + redblock + blackblock
    row = row + redblock + "<br>"
            
    for j in range(0,3):
        row2 = row2 + blackblock + redblock
    row2 = row2 + blackblock + "<br>"
            
    return render_template("index.html", box = (row + row2)*4)


@app.route('/<x>/<y>')
def nextPage(x,y):
    redblock = "<div id='red'></div>"
    blackblock = "<div id='black'></div>"
    row = redblock
    row2 = blackblock
    
    for j in range (1, int(x)):
        if j%2 == 0:
            row = row + redblock
        elif j%2 != 0:
            row = row + blackblock 
    
    for k in range (1, int(x)):
        if k%2 == 0:
            row2 = row2 + blackblock
        elif k%2 != 0:
            row2 = row2 + redblock

    board = row + "<br>"

    for i in range (1, int(y)):
        if i%2 == 0:
            board = board + row + "<br>"
        elif i%2 != 0:
            board = board + row2 + "<br>"

    return render_template("index.html", box = board)
            
if __name__=="__main__":
    app.run(debug=True)

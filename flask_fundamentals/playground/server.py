from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play')
def index():
    return render_template("index.html", bluebox = "<div id='block'></div>"*3)

@app.route('/play/<num>')
def blueByNum(num):
    print(num)
    return render_template("index.html", bluebox = "<div id='block'></div>"*int(num))

@app.route('/play/<num>/<color>')
def boxByNumColor(num, color):
    print(num)
    print(color)
    return render_template("index.html", bluebox = ("<div id='block' style = "+'"background-color:'+ color + ';"'+ "></div>")*int(num))


if __name__=="__main__":
    app.run(debug=True)

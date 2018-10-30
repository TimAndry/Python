from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    message = request.form['message']
    if (request.form['name']) != "" and (request.form['location']) != "" and (request.form['language']) != "":
        return render_template('result.html')
    else:
        print("a user tried to visit /danger. we have redirected the user to /")
        return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
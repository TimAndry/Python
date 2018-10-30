from flask import Flask, render_template, request, redirect, session, flash, url_for
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

mysql = connectToMySQL('leadsnclients')

@app.route('/')
def index():
    all_customers = mysql.query_db("SELECT * FROM customers;")
    names = []
    leads = []
    keys = ["Customer Name", "Number of Leads"]
    for i in range(0, len(all_customers)):
        names.append(all_customers[i]['customer_name'])
    for i in range(0, len(all_customers)):
        leads.append(all_customers[i]['number_of_leads'])
    return render_template('index.html', keys = keys, names = names, leads = leads)



if __name__ == "__main__":
    app.run(debug=True)

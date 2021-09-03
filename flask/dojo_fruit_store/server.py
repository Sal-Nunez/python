from os import name
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
customers = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form['strawberry'], request.form['raspberry'], request.form['apple'], request.form['first_name'], request.form['last_name'], request.form['student_id'])
    count = 0
    customers['strawberry'] = request.form['strawberry']
    customers['raspberry'] = request.form['raspberry']
    customers['apple'] = request.form['apple']
    customers['first_name'] = request.form['first_name']
    customers['last_name'] = request.form['last_name']
    count = int(customers['apple']) + int(customers['strawberry']) + int(customers['raspberry'])
    if request.form['student_id']:
        customers['student_id'] = request.form['student_id']
    elif 'student_id' in customers:
        customers.pop('student_id')
    print(f"Charging {customers['first_name']} for {count} fruits")
    return redirect('/success')

@app.route("/success")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("success.html")

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
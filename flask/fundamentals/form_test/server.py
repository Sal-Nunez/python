from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'wubalubadubdub'
user_list = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form['name'], request.form['email'])
    user_list['name'] = request.form['name']
    user_list['email'] = request.form['email']
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    print(user_list)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html', name_on_template=session['username'], email_on_template=session['useremail'])

if __name__=="__main__":
    app.run(debug=True)
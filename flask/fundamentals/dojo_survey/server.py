from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'wubalubadubdub'
    

@app.route('/')
def index():
    if 'check' in session:
        del session['check']
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['favorite_language'] = request.form['favorite_language']
    session['location'] = request.form['location']
    session['name'] = request.form['name']
    if 'check' in request.form:
        session['check'] = True
    else:
        session['check'] = False
    print(session['check'])
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    forms = {
        'name': session['name'],
        'check': session['check'],
        'location': session['location'],
        'favorite_language': session['favorite_language']
    }
    return render_template('welcome.html', **forms)

if __name__=="__main__":
    app.run(debug=True)
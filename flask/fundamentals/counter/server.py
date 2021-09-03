from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'wubalubadubdub'


@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route('/terminate')
def terminate():
    del session['count']
    return redirect('/')

@app.route('/add2')
def add2():
    session['count'] += 1
    return redirect('/')

@app.route('/addn', methods=['POST'])
def addn ():
    session['number'] = request.form['number']
    session['count'] += (int(session['number'])-1)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
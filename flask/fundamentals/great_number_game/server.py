from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'wubalubadubdub'

@app.route('/')
def index():
    if 'current_display' in session:
        pass
    else:
        session['current_display'] = '|| TAKE A GUESS ||'
    if session['current_display'] == '!CONGRATULATIONS YOU WIN!':
        session['current_display'] = '|| TAKE A GUESS ||'
    if 'winning_number' in session:
        pass
    else:
        session['winning_number'] = random.randint(1, 100)
    return render_template('index.html', current_display=session['current_display'], winning_number=session['winning_number'])

@app.route('/check', methods=['POST'])
def check():
    session['guess'] = request.form['guess']
    print(session['winning_number'])
    if 'tries' not in session:
        session['tries'] = 1
    else:
        session['tries'] += 1
    print(session['tries'])
    if session['tries'] > 4:
        session['current_display'] = "Too Many Guesses YOU LOSE Try Again"
        del session['winning_number']
        del session['tries']
    elif int(session['guess']) > int(session['winning_number']):
        session['current_display'] = '|| TOO BIG GUESS AGAIN ||'
    elif int(session['guess']) < int(session['winning_number']):
        session['current_display'] = '|| TOO small THINK BIGGER ||'
    elif int(session['guess']) == int(session['winning_number']):
        session['current_display'] = '!CONGRATULATIONS YOU WIN! guess my new number'
        del session['winning_number']
    return redirect('/')

@app.route('/reset')
def reset():
    del session['current_display']
    del session['winning_number']
    del session['tries']
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)
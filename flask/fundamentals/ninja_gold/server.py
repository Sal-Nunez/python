from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'wubalubadubdub'



@app.route('/')
def index():
    if 'your_gold' not in session:
        session['your_gold'] = 0
    return render_template('index.html')



@app.route('/process_money', methods=['POST'])
def process_money():
    add()
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

def farm():
    gold_amount = random.randint(10, 20)
    if 'activity' not in session:
        session['activity'] = []
    session['activity'].append(f'<p style= "color: green;">Earned {gold_amount} from the Farm!</p>')
    return gold_amount

def cave():
    gold_amount = random.randint(5, 10)
    if 'activity' not in session:
        session['activity'] = []
    session['activity'].append(f'<p style= "color: green;">Earned {gold_amount} foraging in the odorous Cave!</p>')
    return gold_amount

def house():
    gold_amount = random.randint(2, 5)
    if 'activity' not in session:
        session['activity'] = []
    session['activity'].append(f'<p style= "color: green;">Earned {gold_amount} from sitting around all day</p>')
    return gold_amount

def casino():
    gold_amount = random.randint(0, 50)
    random1 = random.randint(0,1)
    if random1:
        if 'activity' not in session:
            session['activity'] = []
        session['activity'].append(f'<p style= "color: green;">Earned {gold_amount} from the Casino, JACKPOT!!</p>')
        return gold_amount
    else:
        if 'activity' not in session:
            session['activity'] = []
        session['activity'].append(f'<p style= "color: red;">You LOST {gold_amount} from the casino!</p>')
        return (0-gold_amount)

def add():
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        gold_amount = farm()
        session['your_gold'] += gold_amount
    if session['building'] == 'cave':
        gold_amount = cave()
        session['your_gold'] += gold_amount
    if session['building'] == 'house':
        gold_amount = house()
        session['your_gold'] += gold_amount
    if session['building'] == 'casino':
        gold_amount = casino()
        session['your_gold'] += gold_amount
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return None


if __name__=="__main__":
    app.run(debug=True)
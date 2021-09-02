from flask import Flask
from flask import render_template
app = Flask(__name__)

users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

@app.route('/')
def hello_world():
    return render_template('index.html', students=users)

if __name__ == "__main__":
    app.run(debug=True)
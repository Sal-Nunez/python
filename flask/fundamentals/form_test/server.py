from flask import Flask, render_template, request, redirect
app = Flask(__name__)
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
    print(user_list)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
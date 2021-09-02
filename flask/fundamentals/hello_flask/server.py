from flask import Flask  # Import Flask to allow us to create our app
from flask import render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return "success"


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/hello/<banana>')
def hello(banana):
    return f"Hello {banana}"

@app.route('/say/<string:banana>')
def say(banana):
    return f"Hello {banana}"

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/hello1/<string:banana>/<int:num>')
def hello1(banana, num):
    return f"Hello {banana * num}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
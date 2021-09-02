from flask import Flask  # Import Flask to allow us to create our app
from flask import render_template
import math
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
@app.route('/<int:x>/<int:y>/<color1>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>')
@app.route('/')
def checkerboard(x=8, y=8, color1='red', color2='black'):
    return render_template('checkerboard.html', x=int(x/2), y=int(y/2), color1=color1, color2=color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
# Flask

## Virtual Env

1. Go into the folder location of project in terminal
2. Install Flask
    ```
    pipenv install flask
    OR
    python -m pipenv install flask
    ```
3. Open the virtual environment
    ```
    pipenv shell
    OR
    python -m pipenv shell
    ```
4. Creating File Structure -> (MVC)
    ```
    -server.py
    -pipfile
    -pipfile.lock
    -templates
        -index.html
        -js
        -css
5. Server.py File
    ```
    from flask import Flask, render_template, request, redirect
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return render_template('index.html')
    
    if __name__=="__main__":
        app.run(debug=True)
# Notes
    -Routes
        -Display Route -> Render View
        -Action Route -> Perform Action(s)
            - should never display views!!

    -Views -> (mVc) - the V inside (MVC) is views
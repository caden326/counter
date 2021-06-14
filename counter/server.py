from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'gamer'


def sumSessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1


@app.route('/')
def index():
    sumSessionCounter()
    return render_template('index.html')

@app.route('/destroysession')
def destroy():
    session.clear()	
    return render_template('index.html')


if __name__=="__main__":   
        app.run(debug=True)    

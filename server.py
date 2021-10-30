from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'BoomBaby'

@app.route('/')
def visit():
    session['visits'] += int(1) 
    
    if 'visits' in session:
        print('key exists!')
    else:
        print("key 'visits' does NOT exist")
    
    return render_template('index.html')

    session['visits'] = request.form['visits']



if __name__=="__main__":
    app.run(debug=True)
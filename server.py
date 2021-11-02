from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'BoomBaby'

@app.route('/')
def visit():
    if 'visits' in session:
        print('key exists!')
        session['visits'] += int(1) 
    else:
        print("key 'visits' does NOT exist")
        session['visits'] = int(1) 

    return render_template('index.html')


@app.route('/destroy_session')
def reset():
    session['visits'] = int(0)
    return redirect('/')
    
@app.route('/counter')
def counter():
    session['visits'] += int(1)
    return redirect('/')


    session['visits'] = request.form['visits']


if __name__=="__main__":
    app.run(debug=True)
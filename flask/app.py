from flask import Flask,render_template,request
flask=Flask(__name__)
@flask.route('/')
def display():
    if request.method == 'POST':
        if request.form['username']=='admin' and request.form['password']=='1234':
            return render_template('dash.html')
        else:
            return render_template('home.html',error='Invalid credentials')
    return render_template('home.html')
@flask.route('/dashboard')
def dashboard():
    return render_template('dash.html')
if __name__=="__main__":
    flask.run(debug=True)
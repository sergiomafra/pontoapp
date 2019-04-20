from flask import flash, render_template, request, session
from app import app


@app.route('/pontoapp')
def pontoapp():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Hello Boss!'

@app.route('/pontoapp/login', methods=['POST'])
def do_login():
    ## Only testing
    if request.form['password'] == 'password' and \
        request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')

    return pontoapp()

@app.route('/pontoapp/logout')
def do_logout():
    session['logged_in'] = False
    return pontoapp()

if __name__ == '__main__':
    app.run()

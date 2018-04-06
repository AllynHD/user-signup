from flask import Flask, request, redirect, render_template
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('starter-form.html')

@app.route('/', methods=["POST"])
def checker():    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    user_error = ''
    pw_error = ''
    ver_error = ''
    email_error = ''
    
    if len(username) < 3 or len(username) > 20 or " " in username:
        user_error = "BRUH! Username must be between 3 and 20 characters, and no spaces."
    if username == '':
        user_error = "Gotta enter a Username, bruh!"
    if len(password) < 3 or len(password) > 20 or " " in password:
        pw_error = "BRUH! Password must be between 3 and 20 characters, and no spaces."
    if password == '':
        pw_error = "Gotta enter a Password, bruh!"
    if password != verify:
        ver_error = "Bruh, those passwords didn't match."
    if verify == '':
        ver_error = "I think you forgot to verify your password, bruh..."
    if "@" not in email or "." not in email or " " in email:
        email_error = "Bruh, that's not a valid email address. Is you newb?"
    if 3 > len(email) or 20 < len(email):
        email_error = "Email addresses need to be between 3 and 20 characters, bruh..."
    if email == '':
        email_error = ''
    
    if not user_error and not pw_error and not ver_error and not email_error:
        return redirect('/welcome?username=' + username)
    else:
        return render_template('user-form.html', username=username, email=email, user_error=user_error, pw_error=pw_error, ver_error=ver_error, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', name=username)

app.run()
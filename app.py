from flask import Flask, abort, flash, render_template, request, redirect, url_for
from models import User, setup_db, create_db, Toy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
setup_db(app)
create_db()
app.secret_key = 'sikret'

#Home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sign-up', methods=['GET','POST'])
def sign_up():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    age = request.form.get('age')

    if username and email and password and age:

        hash_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

        new_user = User(email=email, username=username, password=hash_password, age=age)
        new_user.add()

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    email_in = request.form.get('email')
    psswd_in = request.form.get('password')

    if email_in and psswd_in:
        user = User.query.filter(User.email==email_in).first()

        if user:
            if check_password_hash(user.password, psswd_in):
                return "<h1>Forbidden user</h1>"

                # return redirect(url_for('home'))
            else:
                # return "<h1>Forbidden user</h1>"
                return redirect(url_for('home'))
        else:
            return redirect(url_for('.login'))

    else:
        print('awesome')
        flash('Wim!')

    return render_template('login.html')

@app.route('/cart')
def cart():

    toys = Toy.query.all()

    return render_template('cart.html', toys = toys)

@app.route('/contact')
def contact():

    return render_template('contact.html')
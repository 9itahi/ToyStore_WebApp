from flask import Flask, flash, render_template, request, redirect, url_for
from models import User, setup_db, create_db, Toy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, current_user, login_required, login_user, login_manager, logout_user

app = Flask(__name__)
setup_db(app)
# create_db()
app.secret_key = 'sikret'

login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Home page
@app.route('/')
def home():
    return render_template('home.html', user=current_user)

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
        flash('Account created succesfully', 'success')

        login_user(new_user)

        return redirect(url_for('home'))

    return render_template('signup.html', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():

    email_in = request.form.get('email')
    psswd_in = request.form.get('password')

    if email_in and psswd_in:
        user = User.query.filter(User.email==email_in).first()

        if user:
            if check_password_hash(user.password, psswd_in):
                login_user(user)
                flash('Login successful','success')
                return redirect(url_for('home'))
            else:
                flash('Wrong password or email','error')
                return redirect(url_for('login'))
        else:
            flash('You simply don\'t belong here', 'error')
            return redirect(url_for('login'))

    else:
        # flash('Please enter a password','error')
        return render_template('login.html', user=current_user)

@app.route('/cart')
@login_required
def cart():

    toys = Toy.query.all()

    return render_template('cart.html', toys = toys, user=current_user)

@app.route('/contact')
def contact():

    return render_template('contact.html', user=current_user)

@app.route('/products')
def products():
    toys = Toy.query.all()
    return render_template('products.html', products=toys, user=current_user)

@app.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('login'))

@app.errorhandler(401)
def unauthorized(error):
    return render_template('404.html')
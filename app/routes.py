# app/main/routes.py

import csv
from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm, SignUpForm
from app.models import User

main_bp = Blueprint('main', __name__)

# Define function to read CSV
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

@main_bp.route('/')
def home():
    file_path = 'app/data/Groceries_dataset.csv'
    grocery_items = read_csv(file_path)
    return render_template('home.html', title='Home', grocery_items=grocery_items)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('main.catalog'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password)
        # Assuming you have a database session and can commit the user
        # db.session.add(user)
        # db.session.commit()
        flash('Sign up successful! Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('signup.html', form=form)

@main_bp.route('/catalog')
def catalog():
    if 'user_id' in session:
        file_path = 'app/data/Groceries_dataset.csv'
        grocery_items = read_csv(file_path)
        return render_template('catalog.html', title='Catalog', grocery_items=grocery_items)
    else:
        flash('Please log in to access the catalog.', 'warning')
        return redirect(url_for('main.login'))

@main_bp.route('/recommendations')
def recommendations():
    items = ["Item 1", "Item 2", "Item 3"]
    return render_template('recommendations.html', items=items)

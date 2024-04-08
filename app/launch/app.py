#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import requests

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = '1234'
login_manager = LoginManager()
login_manager.init_app(app)

# Define a User class for Flask-Login
class User(UserMixin):
    pass

# Define API endpoints for landlord and tenant properties
LANDLORD_PROPERTIES_API = 'https://your-landlord-properties-api.com/properties'
TENANT_PROPERTIES_API = 'https://your-tenant2-properties-api.com/tenants'  # Renamed from 'tenant2'

@login_manager.user_loader
def load_user(user_id):
    # Here, you can add user loading logic using your database
    # For simplicity, we'll just check if the user ID exists in our local users dictionary
    if user_id in users:
        return User()
    return None

@app.route('/')
def index():
    return render_template('app.html', logo_image="images/logoyangu.jpg", landing_page_image="images/WhatsApp Image 2024-04-07 at 10.46.33 PM (1).jpeg", links_images=["images/WhatsApp Image 2024-04-07 at 10.46.33 PM.jpeg", "images/WhatsApp Image 2024-04-07 at 10.46.32 PM (1).jpeg", "images/WhatsApp Image 2024-04-07 at 10.46.32 PM.jpeg"])

@app.route('/properties', methods=['GET', 'POST'])
@login_required
def properties():
    if request.method == 'POST':
        # Get the username and password from the POST request
        username = request.form['username']
        password = request.form['password']

        # Make API calls based on the user type
        if username == 'landlord':
            properties = fetch_properties(LANDLORD_PROPERTIES_API)
        elif username == 'tenant':
            properties = fetch_properties(TENANT_PROPERTIES_API)
        else:
            return 'Invalid username or password', 401

        return render_template('properties.html', properties=properties)
    elif request.method == 'GET':
        # Get the username and password from the URL parameter
        params = request.args
        username = params.get('username')
        password = params.get('password')

        # Make API calls based on the user type
        if username == 'tenant':
            properties = fetch_properties(TENANT_PROPERTIES_API)
        else:
            return 'Invalid username or password', 401

        return render_template('properties.html', properties=properties)

def fetch_properties(api):
    # Make API call to get property data
    response = requests.get(api)
    properties = response.json()
    return properties

@app.route('/tenant', methods=['GET'])
@login_required
def tenant():
    # Get the username and password from the URL parameter
    params = request.args
    username = params.get('username')
    password = params.get('password')

    if username == 'tenant' and password == 'password':
        properties = fetch_properties(TENANT_PROPERTIES_API)
        return render_template('tenant2.html', properties=properties)
    else:
        return 'Invalid username or password', 401

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Here, you can add user creation logic using your database
        # For example, you can create a new user in a database and then authenticate the user

        # For simplicity, we'll just create a local user object
        user = User()
        user.id = username
        user.username = username

        login_user(user)

        return redirect(url_for('properties'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Here, you can add user authentication logic using your database
        # For example, you can check if the username and password match a record in your database

        # For simplicity, we'll just check if the username exists
        if username in users:
            user = User()
            user.id = username
            user.username = username

            login_user(user)

            return redirect(url_for('properties'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0")

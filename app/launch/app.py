#!/usr/bin/python3

from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.url_map.strict_slashes = False

# Define API endpoints for landlord and tenant properties
LANDLORD_PROPERTIES_API = 'https://your-landlord-properties-api.com/properties'
TENANT_PROPERTIES_API = 'https://your-tenant2-properties-api.com/tenants'  # Renamed from 'tenant2'

@app.route('/')
def index():
    return render_template('app.html', logo_image="images/logoyangu.jpg", landing_page_image="images/WhatsApp Image 2024-04-07 at 10.46.33 PM (1).jpeg", links_images=["images/WhatsApp Image 2024-04-07 at 10.46.33 PM.jpeg", "images/WhatsApp Image 2024-04-07 at 10.46.32 PM (1).jpeg", "images/WhatsApp Image 2024-04-07 at 10.46.32 PM.jpeg"])

@app.route('/properties', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(host="0.0.0.0")

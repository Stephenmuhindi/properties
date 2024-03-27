from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Define API endpoints for landlord, tenant, and tenant2 properties
LANDLORD_PROPERTIES_API = 'https://your-landlord-properties-api.com/properties'
TENANT_PROPERTIES_API = 'https://your-tenant-properties-api.com/properties'
TENANT2_PROPERTIES_API = 'https://your-tenant2-properties-api.com/tenants'

@app.route('/')
def index():
    return render_template('app.html')

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
        elif username == 'tenant2':
            properties = fetch_properties(TENANT2_PROPERTIES_API)
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
        elif username == 'tenant2':
            properties = fetch_properties(TENANT2_PROPERTIES_API)
        else:
            return 'Invalid username or password', 401

        return render_template('properties.html', properties=properties)

def fetch_properties(api):
    # Make API call to get property data
    response = requests.get(api)
    properties = response.json()
    return properties

@app.route('/tenant2')
def tenant2():
    # Get the username and password from the URL parameter
    params = request.args
    username = params.get('username')
    password = params.get('password')

    if username == 'tenant2' and password == 'password':
        properties = fetch_properties(TENANT2_PROPERTIES_API)
        return render_template('tenant2.html', properties=properties)
    else:
        return 'Invalid username or password', 401

if __name__ == '__main__':
    app.run(debug=True)

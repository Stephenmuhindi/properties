from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
cnx = mysql.connector.connect(user='your_username', password='your_password', host='your_host', database='your_database')
cursor = cnx.cursor()

# Create the properties table
cursor.execute("""
        CREATE TABLE IF NOT EXISTS properties (
            id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                    address VARCHAR(255) NOT NULL,
                        landlord_id INT NOT NULL,
                            FOREIGN KEY (landlord_id) REFERENCES landlords(id)
                            )
                            """)

# Create the landlords table
cursor.execute("""
        CREATE TABLE IF NOT EXISTS landlords (
            id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL
                        )
                        """)

# Create the tenants table
cursor.execute("""
        CREATE TABLE IF NOT EXISTS tenants (
            id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL,
                            property_id INT NOT NULL,
                                FOREIGN KEY (property_id) REFERENCES properties(id)
                                )
                                """)

# Commit the changes
cnx.commit()

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/properties', methods=['POST'])
    def create_property():
        data = request.get_json()
                name = data.get('name')
                    address = data.get('address')
                        landlord_id = data.get('landlord_id')

                            # Insert the property into the database
                                cursor.execute("INSERT INTO properties (name, address, landlord_id) VALUES (%s, %s, %s)", (name, address, landlord_id))
                                    cnx.commit()

                                        return jsonify({'status': 'success'})

                                    @app.route('/properties', methods=['GET'])
                                    def get_properties():
                                        # Get all properties from the database
                                                cursor.execute("SELECT * FROM properties")
                                                    properties = cursor.fetchall()

                                                        # Convert the properties to JSON
                                                            properties_json = []
                                                                for property in properties:
                                                                    properties_json.append({
                                                                        'id': property[0],
                                                                        'name': property[1],
                                                                        'address': property[2],
                                                                        'landlord_id': property[3]
                                                                        })

                                                                    return jsonify(properties_json)

                                                                @app.route('/tenants', methods=['POST'])
                                                                            def create_tenant():
                                                                                data = request.get_json()
                                                                                        name = data.get('name')
                                                                                            email = data.get('email')
                                                                                                password = data.get('password')
                                                                                                    property_id = data.get('property_id')

                                                                                                        # Insert the tenant into the database
                                                                                                            cursor.execute("INSERT INTO tenants (name, email, password, property_id) VALUES (%s, %s, %s, %s)", (name, email, password, property_id))
                                                                                                                cnx.commit()

                                                                                                                    return jsonify({'status': 'success'})

                                                                                                                @app.route('/tenants', methods=['GET'])
                                                                                                                def get_tenants():
                                                                                                                    # Get all tenants from the database
                                                                                                                            cursor.execute("SELECT * FROM tenants")
                                                                                                                                tenants = cursor.fetchall()

                                                                                                                                    # Convert the tenants to JSON
                                                                                                                                        tenants_json = []
                                                                                                                                            for tenant in tenants:
                                                                                                                                                tenants_json.append({
                                                                                                                                                    'id': tenant[0],
                                                                                                                                                    'name': tenant[1],
                                                                                                                                                    'email': tenant[2],
                                                                                                                                                    'property_id': tenant[3]
                                                                                                                                                    })

                                                                                                                                                return jsonify(tenants_json)

                                                                                                                                            if __name__ == '__main__':
                                                                                                                                                app.run(debug=True)
                                                                                                                                                                from flask import Flask, jsonify, request
                                                                                                                                                                import mysql.connector

                                                                                                                                                                app = Flask(__name__)

                                                                                                                                                                # Connect to MySQL
                                                                                                                                                                cnx = mysql.connector.connect(user='your_username', password='your_password', host='your_host', database='your_database')
                                                                                                                                                                cursor = cnx.cursor()

                                                                                                                                                                # Create the properties table
                                                                                                                                                                cursor.execute("""
                                                                                                                                                                CREATE TABLE IF NOT EXISTS properties (
                                                                                                                                                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                                                                                                                                                        name VARCHAR(255) NOT NULL,
                                                                                                                                                                            address VARCHAR(255) NOT NULL,
                                                                                                                                                                                landlord_id INT NOT NULL,
                                                                                                                                                                                    FOREIGN KEY (landlord_id) REFERENCES landlords(id)
                                                                                                                                                                                    )
                                                                                                                                                                                    """)

                                                                                                                                                                # Create the landlords table
                                                                                                                                                                cursor.execute("""
                                                                                                                                                                CREATE TABLE IF NOT EXISTS landlords (
                                                                                                                                                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                                                                                                                                                        name VARCHAR(255) NOT NULL,
                                                                                                                                                                            email VARCHAR(255) NOT NULL,
                                                                                                                                                                                password VARCHAR(255) NOT NULL
                                                                                                                                                                                )
                                                                                                                                                                                """)

                                                                                                                                                                # Create the tenants table
                                                                                                                                                                cursor.execute("""
                                                                                                                                                                CREATE TABLE IF NOT EXISTS tenants (
                                                                                                                                                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                                                                                                                                                        name VARCHAR(255) NOT NULL,
                                                                                                                                                                            email VARCHAR(255) NOT NULL,
                                                                                                                                                                                password VARCHAR(255) NOT NULL,
                                                                                                                                                                                    property_id INT NOT NULL,
                                                                                                                                                                                        FOREIGN KEY (property_id) REFERENCES properties(id)
                                                                                                                                                                                        )
                                                                                                                                                                                        """)

                                                                                                                                                                # Commit the changes
                                                                                                                                                                cnx.commit()

                                                                                                                                                                @app.route('/')
                                                                                                                                                                def index():
                                                                                                                                                                    return "Hello, World!"

                                                                                                                                                                @app.route('/properties', methods=['POST'])
                                                                                                                                                                    def create_property():
                                                                                                                                                                        data = request.get_json()
                                                                                                                                                                                name = data.get('name')
                                                                                                                                                                                    address = data.get('address')
                                                                                                                                                                                        landlord_id = data.get('landlord_id')

                                                                                                                                                                                            # Insert the property into the database
                                                                                                                                                                                                cursor.execute("INSERT INTO properties (name, address, landlord_id) VALUES (%s, %s, %s)", (name, address, landlord_id))
                                                                                                                                                                                                    cnx.commit()

                                                                                                                                                                                                        return jsonify({'status': 'success'})

                                                                                                                                                                                                    @app.route('/properties', methods=['GET'])
                                                                                                                                                                                                    def get_properties():
                                                                                                                                                                                                        # Get all properties from the database
                                                                                                                                                                                                                cursor.execute("SELECT * FROM properties")
                                                                                                                                                                                                                    properties = cursor.fetchall()

                                                                                                                                                                                                                        # Convert the properties to JSON
                                                                                                                                                                                                                            properties_json = []
                                                                                                                                                                                                                                for property in properties:
                                                                                                                                                                                                                                    properties_json.append({
                                                                                                                                                                                                                                        'id': property[0],
                                                                                                                                                                                                                                        'name': property[1],
                                                                                                                                                                                                                                        'address': property[2],
                                                                                                                                                                                                                                        'landlord_id': property[3]
                                                                                                                                                                                                                                        })

                                                                                                                                                                                                                                    return jsonify(properties_json)

                                                                                                                                                                                                                                @app.route('/tenants', methods=['POST'])
                                                                                                                                                                                                                                            def create_tenant():
                                                                                                                                                                                                                                                data = request.get_json()
                                                                                                                                                                                                                                                        name = data.get('name')
                                                                                                                                                                                                                                                            email = data.get('email')
                                                                                                                                                                                                                                                                password = data.get('password')
                                                                                                                                                                                                                                                                    property_id = data.get('property_id')

                                                                                                                                                                                                                                                                        # Insert the tenant into the database
                                                                                                                                                                                                                                                                            cursor.execute("INSERT INTO tenants (name, email, password, property_id) VALUES (%s, %s, %s, %s)", (name, email, password, property_id))
                                                                                                                                                                                                                                                                                cnx.commit()

                                                                                                                                                                                                                                                                                    return jsonify({'status': 'success'})

                                                                                                                                                                                                                                                                                @app.route('/tenants', methods=['GET'])
                                                                                                                                                                                                                                                                                def get_tenants():
                                                                                                                                                                                                                                                                                    # Get all tenants from the database
                                                                                                                                                                                                                                                                                            cursor.execute("SELECT * FROM tenants")
                                                                                                                                                                                                                                                                                                tenants = cursor.fetchall()

                                                                                                                                                                                                                                                                                                    # Convert the tenants to JSON
                                                                                                                                                                                                                                                                                                        tenants_json = []
                                                                                                                                                                                                                                                                                                            for tenant in tenants:
                                                                                                                                                                                                                                                                                                                tenants_json.append({
                                                                                                                                                                                                                                                                                                                    'id': tenant[0],
                                                                                                                                                                                                                                                                                                                    'name': tenant[1],
                                                                                                                                                                                                                                                                                                                    'email': tenant[2],
                                                                                                                                                                                                                                                                                                                    'property_id': tenant[3]
                                                                                                                                                                                                                                                                                                                    })

                                                                                                                                                                                                                                                                                                                return jsonify(tenants_json)

                                                                                                                                                                                                                                                                                                            if __name__ == '__main__':
                                                                                                                                                                                                                                                                                                                app.run(debug=True)


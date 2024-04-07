#!/usr/bin/python3
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
        )

# Routes
@app.route('/properties', methods=['GET'])
def get_properties():
    cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM properties")
                properties = cursor.fetchall()
                    cursor.close()
                        return jsonify(properties)


                    @app.route('/properties', methods=['POST'])
                    def add_property():
                        data = request.json
                        title = data.get('title')
                        description = data.get('description')
                        price = data.get('price')
                        cursor = db.cursor()
                        cursor.execute("INSERT INTO properties (title, description, price) VALUES (%s, %s, %s)", (title, description, price))
                        db.commit()
                        cursor.close()
                        return jsonify({"message": "Property added successfully"})


                    @app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
                    def signup():
                        if request.method == 'POST':
                            pass
                        else:
                            pass
                        if __name__ == '__main__':
                            app.run(debug=True)


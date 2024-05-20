from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL database connection settings
db_config = {
    'user': 'admin',    # <-- Change this
    'password': 'xxxxxxxx',    # <-- Change this
    'host': 'database-1.c3djsfi88999.us-east-2.rds.amazonaws.com',   # <-- Change this
    'database': 'gog'   # <-- Change this
}
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # <-- Change this replace 'your_form.html' with the name of your HTML file

@app.route('/submit', methods=['POST'])

def submit_form():
    name = request.form['name']
    email = request.form['email']

    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Insert the form data into the database
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"     # <-- Change this into your table name which you have created in mysql
    values = (name, email)
    cursor.execute(query, values)
    cnx.commit()

    cursor.close()
    cnx.close()

    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

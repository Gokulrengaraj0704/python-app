from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL database connection settings
db_config = {
    'user': 'admin',
    'password': '12345678',
    'host': 'database-1.c3y8am2gya2m.us-east-2.rds.amazonaws.com',
    'database': 'gokul'
}
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # replace 'your_form.html' with the name of your HTML file

@app.route('/submit', methods=['POST'])

def submit_form():
    name = request.form['name']
    email = request.form['email']

    # Connect to the MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Insert the form data into the database
    query = "INSERT INTO data (Name, Email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(query, values)
    cnx.commit()

    cursor.close()
    cnx.close()

    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

'''# MySQL configuration
db = mysql.connector.connect(
  host="your-rds-endpoint",
  user="your-username",
  password="your-password",
  database="your-database"
)
'''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    cursor = db.cursor()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(query, values)
    db.commit()

    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
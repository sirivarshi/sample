from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Siri@131211'
app.config['MYSQL_DB'] = 'employee'

db = MySQL(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    gmail = db.Column(db.String(120), unique=True, nullable=False)
@app.route('/')
def index():
    fname = "hyma"
    email = "gunupatihymavathi04@gmail.com"
    entry = User(name = fname,gmail = email)
    print("hi")
    db.session.add(entry)
    db.session.commit()
    print("successfully executed")

if __name__ == "__main__":
    app.run(host='localhost', port=3306)






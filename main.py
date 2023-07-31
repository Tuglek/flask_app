import requests as requests
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "H"
@app.route('/primes/<int:a>')
def fibon(a):
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
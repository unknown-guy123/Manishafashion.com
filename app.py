from flask import Flask, render_template, url_for
import psycopg2

app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def index():
    return render_template('index.html')

def database():
    conn = psycopg2.connect(
        dbname="postgres",
        user="web_owner",
        password="owner@123",
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

if (__name__) == '__main__':
    app.run(debug=True)
import json
from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
import chatbot
import main


app = Flask(__name__)
app.secret_key = 'your_secret_key'
client = MongoClient('mongodb://localhost:27017/')  # MongoDB connection
db = client['wellbeing']  # Database name
collection = db['well-being']  # Collection name

@app.route('/')
def home():
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = collection.find_one({'username': username, 'password': password})
    if user:
        session['logged_in'] = True
        return redirect('/val')
    else:
        return render_template('login.html', error='Invalid credentials')




@app.route('/val')
def validate():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('index.html')




@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return redirect('/')




@app.route('/reg', methods=['GET'])
def new_user():
    return render_template('register.html')

@app.route('/guest', methods=['GET'])
def guest():
    return render_template('index copy.html')




@app.route('/reg', methods=['POST'])
def register():
    username = request.form['username']
    mail = request.form['mail']
    password = request.form['password']
    age = request.form['age']

    existing_user = collection.find_one({'username': username})
    if existing_user:
        return render_template('register.html', error='Username already exists')
    user = {
        'username': username,
        'password': password,
        'mail': mail,
        'age' : age
    }
    collection.insert_one(user)

    session['logged_in'] = True
    return render_template('index.html')

with open('intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

@app.route('/chat', methods=['POST'])
def chat():
    if not session.get('logged_in'):
        return redirect('/')
    else :
        message = request.form['user_input']
        querys= message
        intent = chatbot.predict_class(message)
        response = chatbot.get_response(intent, intents)
        if response is not None:
            return render_template('index.html', user_input=message, response=response, query=querys)
        else:
            return render_template('index.html', user_input=message, response="Sorry, I didnt understand.", query=querys)
        

@app.route('/chat1', methods=['POST'])
def chat1():
    message = request.form['user_input']
    querys= message
    response = main.match_response(message)
    if response is not None:
        return render_template('index copy.html', user_input=message, response=response, query=querys)
    else:
        return render_template('index copy.html', user_input=message, response="Sorry, I didnt understand.", query=querys)
    


if __name__ == '__main__':
    app.run()

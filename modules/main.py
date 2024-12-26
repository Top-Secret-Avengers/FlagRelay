from flask import Flask, jsonify, request, render_template

from reader import getAnswers, getHints
from helper import addPlayer

app = Flask(__name__, template_folder='../templates', static_folder="../static")

answers = getAnswers()
hints = getHints()
players = {}

#Use this to return the home page, with the leaderboard and whatever else we want. if not logged in send them to /login instead
@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        return render_template('index.html')
    
# login route, add them to leaderboard 
@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            print('No data provided')
        userInput = data.get('input')
        if userInput:
            if addPlayer(userInput,players):
                print(players)
                return jsonify({"woohoo": "you did it"}), 201
            else:
                return jsonify({"error": "name taken"}), 400
# need route for submitting answer, somehow have userId and other stuff using json body, limit amount you can send at a time

# need route for admin page to remove users and reveal hints
@app.route('/admin', methods = ['GET'])
def admin():
    return False

# need route to see hints unless we put on homepage

#boilerplate, makes flask projects run
if __name__ == '__main__':
    app.run()
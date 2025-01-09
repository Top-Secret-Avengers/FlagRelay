from flask import Flask, jsonify, request, render_template

from reader import getAnswers, getHints
from helper import addPlayer, submitScore

app = Flask(__name__, template_folder='../templates', static_folder="../static")
# use a dictionary with answers to have the answer as a key and a list of player names as the value
answers = getAnswers()
hints = getHints()
players = {}

#Use this to return the home page, with the leaderboard and hints. if not logged in send them to /login instead
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
        # none data type is falsey. return 400
        if not data:
            print('No data provided')
            return jsonify({"error": "no data provided"}), 400
        userInput = data.get('input')
        if userInput:
            if addPlayer(userInput,players):
                print(players)
                return jsonify({"woohoo": "you did it"}), 201
            else:
                return jsonify({"error": "name taken"}), 400
# need route for submitting answer, somehow have userId and other stuff using json body, limit amount you can send at a time
@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        # turn json into python objects we can use
        data = request.get_json()
        user = request.cookies.get('loggedin')
        # check if Post is valid
        if not data or user not in players:
            return jsonify({"error": "flag incorrect or player not logged in"}), 400
        flag = data.get('flag')
        #we will do something special for more valuable flags, for now this works
        if submitScore(flag, user, 1, answers, players):
            return jsonify({'flag correct': "flag correct!"}), 200
    
    return jsonify({'error': "bad route"}), 400
# need route for admin page to remove users and reveal hints
@app.route('/admin', methods = ['GET'])
def admin():
    return False

#boilerplate, makes flask projects run
if __name__ == '__main__':
    app.run()
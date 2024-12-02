from flask import Flask, jsonify, request

app = Flask(__name__)


#Use this to return the home page, with the leaderboard and whatever else we want
@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        data = "test"
        return jsonify({'data':data})
    
# login route, add them to leaderboard 
@app.route('/login' methods = ['POST'])
def login():
    
# need route for submitting answer, somehow have userId and other shit using cookies


# need route for admin page to remove users and reveal hints

# need route to see hints unless we put on homepage


#boilerplate, makes flask projects run
if __name__ == '__main__':
    app.run()
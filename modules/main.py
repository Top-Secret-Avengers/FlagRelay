from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='../templates')


#Use this to return the home page, with the leaderboard and whatever else we want. if not logged in send them to /login instead
@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        return render_template('index.html')
    
# login route, add them to leaderboard 
@app.route('/login', methods = ['POST'])
def login():
    return False
    
# need route for submitting answer, somehow have userId and other shit using json body, limit amount you can send at a time

# need route for admin page to remove users and reveal hints
@app.route('admin', methods = 'GET')
def admin():
    return False

# need route to see hints unless we put on homepage

#boilerplate, makes flask projects run
if __name__ == '__main__':
    app.run()
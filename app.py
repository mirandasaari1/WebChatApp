import os
import flask
import flask_socketio
#from sqlalchemy import *
#import flask_sqlalchemy
#import models
import requests
import requests.auth



app = flask.Flask(__name__)
# URI scheme: postgresql://<username>:<password>@<hostname>:<port>/<database-name>
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLalchemy(app)
socketio = flask_socketio.SocketIO(app)



@app.route('/')
    

def hello(): 
#accessing keys
    #config vars
    # twilio_id = 	os.getenv("twilio_id"),
    # twilio_secret = 	os.getenv("twilio_secret")
    # api_auth = requests.auth.HTTPBasicAuth(twilio_id,twilio_secret)
    
# def index():
#     messages = models.Message.query.all()
#     html = ['<li>' + m.text + '</li>' for m in messages]
#     return '<ul>' + ''.join(html) + '</ul>'
    return flask.render_template('myindex.html')



#wraps the app
@socketio.on('connect')
def on_connect():
    #print 'Someone connected!'
    socketio.emit('user:join', 'Mir')

@socketio.on('disconnect')
def on_disconnect():
    socketio.emit('user:left', 'Mir')
    
@socketio.on('send:message')
def send_message(data):
    socketio.emit('send:message', data, broadcast=True, include_self=False);
    if(data["text"].startswith("!!")):
        # print("X" * 50)
        if(data["text"].startswith("!!about")):
            server_data={"text":"Hi friends! welcome to the chat room, share your thoughts with your friends!", "user":"chatbot"};
        elif(data["text"].startswith("!!help")):
            server_data={"text":"Try: !!about !!help !!joke !!funfact, !!sms", "user":"chatbot"};
        elif(data["text"].startswith("!!say")):
            substring=data["text"][5:]
            server_data={"text":substring, "user":"chatbot"};
        elif(data["text"].startswith("!!joke")):
            server_data={"text":"you have the nicest syntax ive ever seen", "user":"chatbot"};
        elif(data["text"].startswith("!!funfact")):
            server_data={"text":"bananas are curved because they grow towards the sun", "user":"chatbot"};
        elif(data["text"].startswith("!!sms")):
            server_data={"text":"Tell me who I am sending to and what I am saying! Follow this format: #XXXXXXXXXX message"};
        elif(data["text"].startswith("!!")):
            server_data={"text":"Sorry! I dont know this command, try !!help", "user":"chatbot"};
        print(server_data)
        socketio.emit('send:message', server_data, broadcast=True)
    #reads user phone number and text
    elif(data["text"].startswith("#")):
        message_body=data["text"][12:]
        number=data["text"][1:11]
        server_data={"text":"I sent your message!", "user":"chatbot"};
        socketio.emit('send:message', server_data, broadcast=True)
        api_auth=requests.auth.HTTPBasicAuth(
            'ACf5b90a591a358475b17c29aa99d3f581',
            'e85e42238ad5d0c6ea1d5b9cca398411'
        )
        api_data={
            'From':'+19717173469',
            'To': '+1' + number,
            'Body': message_body
            
        }
        response = requests.post(
            'https://api.twilio.com/2010-04-01/Accounts/ACf5b90a591a358475b17c29aa99d3f581/Messages.json',
            auth = api_auth,
            data = api_data
        )
        print response.text
    
def get_chatbot_response(data):
    if(data.startswith("!!")):
        if(data.startswith("!!about")):
            return "Hi friends! welcome to the chat room, share your thoughts with your friends!";
        elif(data.startswith("!!help")):
            return "Try: !!about !!help !!joke !!funfact, !!sms";
        elif(data.startswith("!!say")):
            substring=data[5:]
            return substring;
        elif(data.startswith("!!joke")):
            return "you have the nicest syntax ive ever seen";
        elif(data.startswith("!!funfact")):
            return "bananas are curved because they grow towards the sun";
        elif(data.startswith("!!sms")):
            return "Tell me who I am sending to and what I am saying! Follow this format: #XXXXXXXXXX message";
        elif(data.startswith("!!")):
            return "Sorry! I dont know this command, try: !!help";
    elif(data.startswith("#")):
        return "I sent your message!";

# @socketio.on('dbconnect')
# def sned_database(data):
#     socketio.emit('dbconnect', data)
    
if __name__ == '__main__': # __name__!
    socketio.run(
     app,
     host=os.getenv('IP', '0.0.0.0'),
     port=int(os.getenv('PORT', 8080)),
     debug=True
    )


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     message = db.Column(db.Text, unique=True)
#     timestamp = db.Column(db.DateTime)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username
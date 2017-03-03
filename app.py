import os
import flask
import flask_socketio
#from sqlalchemy import *
#import flask_sqlalchemy
#import models


app = flask.Flask(__name__)
# URI scheme: postgresql://<username>:<password>@<hostname>:<port>/<database-name>
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLalchemy(app)
socketio = flask_socketio.SocketIO(app)



@app.route('/')
def hello(): 
    return flask.render_template('myindex.html')
    
# def index():
#     messages = models.Message.query.all()
#     html = ['<li>' + m.text + '</li>' for m in messages]
#     return '<ul>' + ''.join(html) + '</ul>'



#wraps the app
@socketio.on('connect')
def on_connect():
    print 'Someone connected!'
    socketio.emit('user:join', 'Mir')
#  flask_socketio.emit('update', {
#  'data': 'Got your connection!'
#  })

@socketio.on('disconnect')
def on_disconnect():
    socketio.emit('user:left', 'Mir')
    
@socketio.on('send:message')
def send_message(data):
    socketio.emit('send:message', data, broadcast=True, include_self=False);
    if(data["text"].startswith("!!")):
        print("X" * 50)
        if(data["text"].startswith("!!about")):
            server_data={"text":"Hi friends! welcome to the chat room, share your thoughts with your friends!", "user":"chatbot"};
        elif(data["text"].startswith("!!help")):
            server_data={"text":"Try: !!about !!help !!joke !!funfact", "user":"chatbot"};
        elif(data["text"].startswith("!!say")):
            substring=data["text"][5:]
            server_data={"text":substring, "user":"chatbot"};
        elif(data["text"].startswith("!!joke")):
            server_data={"text":"'you have the nicest syntax ive ever seen", "user":"chatbot"};
        elif(data["text"].startswith("!!funfact")):
            server_data={"text":"bananas are curved because they grow towards the sun", "user":"chatbot"};
        elif(data["text"].startswith("!!")):
            server_data={"text":"Sorry! don't know this command, try !!help", "user":"chatbot"};
        print(server_data)
        socketio.emit('send:message', server_data, broadcast=True)
        
 
    
# @socketio.on('dbconnect')
# def sned_database(data):
#     socketio.emit('dbconnect', data)
    
#if __name__ == '__main__': # __name__!
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
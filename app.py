import os
import flask
import flask_socketio
#from sqlalchemy import *


app = flask.Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLalchemy(app)
socketio = flask_socketio.SocketIO(app)


@app.route('/')
def hello(): 
    return flask.render_template('myindex.html')


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
    socketio.emit('send:message', data, broadcast=True, include_self=False)
    

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
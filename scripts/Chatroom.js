import React, {Component} from 'react';
import * as SocketIO from 'socket.io-client';

var socket=SocketIO.connect();

//userList
var UsersList = React.createClass({
  render() {
      return (
          <div className='users'>
              <h3> Online Users: {this.props.users.length} </h3>
              <ul>
                  {
                      this.props.users.map((user, i) => {
                          return (
                              <li key={i}>
                                  {user}
                              </li>
                          );
                      })
                  }
              </ul>                
          </div>
      );
  }
})

//Message 
var Message = React.createClass({
  render() {
      return (
          <div className="message">
              <strong>{this.props.user}: </strong> 
              <span>{this.props.text}</span>        
          </div>
      );
  }
})

//and MessageList
var MessageList = React.createClass({
  render() {
      return (
          <div className='messages'>
              <h2> Conversation: </h2>
              {
                  this.props.messages.map((message, i) => {
                      return (
                          <Message
                              key={i}
                              user={message.user}
                              text={message.text}
                          />
                      );
                  })
              }
          </div>
      );
  }
});
//messageForm
var MessageForm = React.createClass({

  getInitialState() {
      return {text: ''};
  },

  handleSubmit(e) {
      e.preventDefault();
      var message = {
          user : this.props.user,
          text : this.state.text
      }
      this.props.onMessageSubmit(message); 
      this.setState({ text: '' });
  },
//bot checks the message
  checkMessage(e){
    e.preventDefault();
    var recievedMessage = this.state.text;
    var botResponse;
    if(recievedMessage.startsWith("!!")){
        if(recievedMessage.startsWith("!!about")){
            botResponse="Hi friends! welcome to the chat room, share your thoughts with your friends!";
        }
        else if(recievedMessage.startsWith("!!help")){
            botResponse="Try: !!about !!help !!joke !!funfact";
        }
        else if(recievedMessage.startsWith("!!say")){
            botResponse="'message.substring(6)";
        }
        else if(recievedMessage.startsWith("!!joke")){
           botResponse="'you have the nicest syntax ive ever seen";
        }
        else if(recievedMessage.startsWith("!!funfact")){
           botResponse="bananas are curved because they grow towards the sun";
        }
        else if(recievedMessage.startsWith("!!")){
           botResponse="Sorry! don't know this command, try !!help";
        }
    }
    var message = {
      user : 'Chatbot',
      text : botResponse
    }
    this.props.onBotMessage(message); 
    this.setState({ text: '' });
  },

  changeHandler(e) {
      this.setState({ text : e.target.value });
  },

  render() {
      return(
          <div className='message_form'>
              <h3>Write New Message</h3>
              <form onSubmit={this.handleSubmit, this.checkMessage}>
                  <input
                      onChange={this.changeHandler}
                      value={this.state.text}
                  />
              </form>
          </div>
      );
  }
});


//chatApp
var ChatApp = React.createClass({

  getInitialState() {
      return {users: [], messages:[], text: ''};
  },

  componentDidMount() {
      socket.on('init', this._initialize);
      socket.on('send:message', this._messageRecieve);
      socket.on('user:join', this._userJoined);
      socket.on('user:left', this._userLeft);
     // socket.on('change:name', this._userChangedName);
  },

  _initialize(data) {
      var {users, name} = data;
      this.setState({users, user: name});
  },

  _messageRecieve(message) {
      var {messages} = this.state;
      messages.push(message);
      this.setState({messages});
  },

  _userJoined(data) {
      var {users, messages} = this.state;
      var name= data;
     
      users.push(name);
      messages.push({
          user: 'CHATBOT',
          text : name +' Joined'
      });
      this.setState({users, messages});
  },

  _userLeft(data) {
      var {users, messages} = this.state;
      var name = data;
      var index = users.indexOf(name);
      users.splice(index, 1);
      messages.push({
          user: 'CHATBOT',
          text : name +' Left'
      });
      this.setState({users, messages});
  },

  handleMessageSubmit(message) {
      var {messages} = this.state;
      messages.push(message);
      this.setState({messages});
      socket.emit('send:message', message);
  },

   render() {
  //   const notes = this.props.notes;
  //   const style = {
  //   margin: '0.5em',
  //   paddingLeft: 0,
  //   listStyle: 'none'
  // };
      return (
          <div>
              <UsersList
                  users={this.state.users}
              />
              <MessageList
                  messages={this.state.messages}
              />
              <MessageForm
                  onMessageSubmit={this.handleMessageSubmit}
                  onBotMessage={this.handleMessageSubmit}
                  user = "Mir"
                  //user={this.state.user}
              />
          </div>
      );
  }
});



export class Chatroom extends React.Component{
  render(){
    return(
    <div className="Chat">
          <ChatApp/>
    </div>
    );
  }
}

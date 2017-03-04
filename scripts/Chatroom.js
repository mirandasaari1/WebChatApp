import React, {Component} from 'react';
import * as SocketIO from 'socket.io-client';
//import models

var socket=SocketIO.connect();

//userList
var UsersList = React.createClass({
  render() {
      return (
          <div className='msg-wgt-header'>
          
              <h3> Online Users: {this.props.users.length} </h3>
              <ul>
                  {
                      this.props.users.map((user, i) => {
                          return (
                              <li key={i}>
                              <a href="#">{user}</a>
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
    var message=this.props.text;
    var message1="";
    if(message.toLowerCase().includes("http://") || message.toLowerCase().includes("https://")){
      if(message.toLowerCase().includes(".jpg")){
        console.log("jpg");
        console.log(message);
        message1=<img src={message} width="200px"/>;
      }
      else if(message.toLowerCase().includes(".jpeg")){
        console.log("jpeg");
        message1=<img src={message} width="200px"/>;
      }
      else if(message.toLowerCase().includes(".png")){
        console.log("png");
        message1=<img src={message} width="200px"/>;
      }
      else if(message.toLowerCase().includes(".gif")){
        console.log("gif");
        message1=<img src={message} width="200px"/>;
      }
      else{
        message1=<a href={message}>{message}</a>;
      }
    }
    else{
      message1=<p>{message}</p>;
    }
      return (
           <div className="msg-row-container">
            <div className="msg-row">
            <span className="user-label">
            <a href="#" className="chat-username">{this.props.user}</a>
              </span><br/>
              <div>{message1}</div>  
              </div>
          </div>
      );
    }
});

//and MessageList
var MessageList = React.createClass({
  render() {
    var inlineStyles = {
      height: '300px',
      overflowY: 'scroll'
    };
      return (
         <div style={inlineStyles}>
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

  changeHandler(e) {
      this.setState({ text : e.target.value });
  },
  
  _initialize(data){
    var{users,name} = data;
    this.setState({users, user: name});
  },
  
  render() {
      return(
          <div className='msg-wgt-footer'>
              <h3>Write New Message</h3>
              <form onSubmit={this.handleSubmit}>
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
      socket.on('send:message', (d) => {this._messageRecieve(d); });
      socket.on('user:join', this._userJoined);
      socket.on('user:left', this._userLeft);
  },

  _initialize(data) {
      var {users, name} = data;
      this.setState({users, user: name});
  },

  _messageRecieve(message) {
      var {messages} = this.state;
      console.log(message);
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
  
//database send
  // handleDatabaseSend(message){
  //   models.db.session.add(user)
  //   models.db.session.add(message)
  //   models.db.session.add(image_url)
  //   models.db.session.commit()
  // },

   render() {
      return (
          //<div>
          <div className="chat-container">
              <UsersList
                  users={this.state.users}
              />
              <MessageList
                  messages={this.state.messages}
              />
              <MessageForm
                  onMessageSubmit={this.handleMessageSubmit}
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


// FB.getLoginStatus((response) => {
//   if (response.status == 'connected') {
//   socket.emit('new number', {
//   'facebook_user_token':
//   response.authResponse.accessToken,
//   'number': random,
//   });
//   }
// });

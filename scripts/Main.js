import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { Content } from './Content';
import { Chatroom } from './Chatroom';
import { Socket } from './Socket';

ReactDOM.render(<Chatroom />, document.getElementById('content'));
//ReactDOM.render(<Content />, document.getElementById('content'));

Socket.on('connect', function() {
 console.log('Connecting to the server!');
})


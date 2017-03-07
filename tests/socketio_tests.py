import app, unittest, requests

class SocketIOTestCase(unittest.TestCase):
    
#tests socket on connect    
    def test_server_sends_connection(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        # print r
        self.assertEquals(len(r), 1)
        from_server = r[0]
        # self.assertEquals(
        #     from_server ['CHATBOT'], 
        #     'Mir Joined'
        # )
        data = from_server['args'][0]
        # print data
        self.assertEquals(data, 'Mir')
        
#tests socket on disconnect
    def test_server_sends_disconnect(self):
        client = app.socketio.test_client(app.app)
        r = client.get_received()
        #print r
        self.assertEquals(len(r), 1)
        from_server = r[0]
        data = from_server['args'][0]
        # print data
        self.assertEquals(data, 'Mir')

#tests socket on send:message
#makes sure server sends out but not on the local server
    def test_server_relays_message(self):
            client = app.socketio.test_client(app.app)
            test_message={u'text': u'test message', u'user': u'Mir'}
            client.emit('send:message', test_message)
            r = client.get_received()
            # print "r is", r
            self.assertEquals(len(r), 1)
            # from_server = r[0]
            # self.assertEquals(
            #     from_server['name'],
            #     'got your message'
            # )
            # data = from_server['args'][0]
            # print "Here we are!!!";
            # print data
            # self.assertEquals(
            #     data,
            #     u'test message'
            # )
#tests the chatbot responds correctly to 
    def test_server_relays_chatbot_message(self):
            client = app.socketio.test_client(app.app)
            test_message={u'text': u'!!Potatoes are cool!', u'user': u'Mir'}
            client.emit('send:message', test_message)
            r = client.get_received()
            # print "r is ", r
            # print "r is done"
            self.assertEquals(len(r), 2)
            from_server = r[1]
            # self.assertEquals(
            #     from_server['name'],
            #     'got your message'
            # )
            data = from_server['args'][0]
            # print "data is ", data
            self.assertEquals(
                data['text'],
                u'Sorry! I dont know this command, try !!help'
            )
            
    def test_server_reads_phone_number_message(self):
            client = app.socketio.test_client(app.app)
            test_message={u'text': u'#5037537079 hey there from chat app', u'user': u'Mir'}
            client.emit('send:message', test_message)
            r = client.get_received()
            # print "r is ", r
            # print "r is done"
            self.assertEquals(len(r), 2)
            from_server = r[1]
            # self.assertEquals(
            #     from_server['name'],
            #     'got your message'
            # )
            data = from_server['args'][0]
           # print "data is ", data
            self.assertEquals(
                data['text'],
                u'I sent your message!'
            )
            
if __name__ == '__main__':
    unittest.main()
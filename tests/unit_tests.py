import unittest
import app

class ChatBotResponseTest(unittest.TestCase):
    def test_about_command(self):
        response = app.get_chatbot_response('!!about')
        self.assertEquals(response, "Hi friends! welcome to the chat room, share your thoughts with your friends!")
        
    def test_help_command(self):
        response = app.get_chatbot_response('!!help')
        self.assertEquals(response, "Try: !!about !!help !!joke !!funfact, !!sms")
        
    def test_sms_command(self):
        response = app.get_chatbot_response('!!sms')
        self.assertEquals(response, "Tell me who I am sending to and what I am saying! Follow this format: #XXXXXXXXXX message")
        
    def test_joke_command(self):
        response = app.get_chatbot_response('!!joke')
        self.assertEquals(response, "you have the nicest syntax ive ever seen")
        
    def test_say_command(self):
        response = app.get_chatbot_response('!!say something')
        self.assertEquals(response, " something")
        
    def test_funfact_command(self):
        response = app.get_chatbot_response('!!funfact')
        self.assertEquals(response, "bananas are curved because they grow towards the sun")
        
    def test_not_command(self):
        response = app.get_chatbot_response('!!yolo')
        self.assertEquals(response, "Sorry! I dont know this command, try: !!help")
    
    def test_response_command(self):
        response = app.get_chatbot_response('#5037537079 hello')
        self.assertEquals(response, "I sent your message!")
        
    def test_wrong_command(self):
        response = app.get_chatbot_response('!!!!!!!')
        self.assertEquals(response, "Sorry! I dont know this command, try: !!help")
        
    def test_say_anothercommand(self):
        response = app.get_chatbot_response('!!say wahooooooo')
        self.assertEquals(response, " wahooooooo")
        
    
        
if __name__ == '__main__':
    unittest.main()
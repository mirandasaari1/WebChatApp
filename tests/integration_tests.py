import app, unittest, flask_testing, requests
from flask_testing import TestCase
import urllib2
from flask import Flask
from flask_testing import LiveServerTestCase
from flask.ext.testing import TestCase

template = """<html>

<head>
    <style>
    
.msg-wgt-header {
  background-color: #90949b;
  border-radius: 25px;
  opacity: 0.7;
  border: 1px solid rgba(55, 57, 61);
  border-top-right-radius: 3px;
  border-top-left-radius: 3px;
  color: white;
  text-align: left;
  height: auto;
  width:200px;
}

.msg-wgt-header a {
  text-decoration: none;
  font-weight: bold;
  color: white;
  vertical-align: middle;
}

/* message box body styles*/

.msg-row-container {
  border-bottom: 1px solid lightgray;
  background-color:#f0f0f5;
  opacity: 0.7;
}

.msg-row {
  width: 75%;
  display: inline-block;
}

.message {
  margin-left: 40px;
  margin-right: 40px;
}

/* Message box footer styles*/

.msg-wgt-footer {
  height: 42px;
}

.msg-wgt-footer textarea {
  width: 95%;
  height: 42px;
  font-family: 'tahoma';
  font-size: 13px;
  padding: 5px;
}

.user-label {
  font-size: 11px;
}

.chat-username {
    
  color: '#5b5e63';
}

.msg-time {
  font-size: 10px;
  float: right;
  color: gray;
}

.avatar {
  width: 30px;
  height: 30px;
  float: left;
  background: url('/chat/public/assets/chat_avatar.png');
  border: 1px solid lightgray;
}
    </style>
<!--<link href="css/main.css" rel="stylesheet" type="text/css" />-->
<script src="https://apis.google.com/js/platform.js" async defer></script>
<meta name="google-signin-client_id" content="958439215720-st63sjm24qfbo95ljeovg37e9sv0jcq3.apps.googleusercontent.com">
</head>

<body>
    <style>
    body{
    background-image: url('https://upload.wikimedia.org/wikipedia/commons/4/49/Water_splashes_001.jpg');
    background-size:cover;
    }
    </style>
    
    <!--google login button -->
    <div class="g-signin2" data-onsuccess="onSignIn"></div>
    <!-- facebook button -->
    <br>
    <div class="fb-login-button" data-max-rows="1" data-size="xlarge" data-show-faces="false" data-auto-logout-link="false"></div>
    <!--Facebook login -->
    <div id="fb-root"></div>
    <script>(function(d, s, id) {
          var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) return;
          js = d.createElement(s); js.id = id;
          js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.8&appId=1957124057863332";
          fjs.parentNode.insertBefore(js, fjs);
            }
        (document, 'script', 'facebook-jssdk'));
    </script>
  <script>
      window.fbAsyncInit = function() {
        FB.init({
          appId      : '1840446522877181',
          xfbml      : true,
          version    : 'v2.8'
        });
        FB.AppEvents.logPageView();
      };
    
      (function(d, s, id){
         var js, fjs = d.getElementsByTagName(s)[0];
         if (d.getElementById(id)) {return;}
         js = d.createElement(s); js.id = id;
         js.src = "//connect.facebook.net/en_US/sdk.js";
         fjs.parentNode.insertBefore(js, fjs);
       }(document, 'script', 'facebook-jssdk'));
    </script>
    
<!------------------------------------------------->
<!--google -->
<script>
function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  //console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
 // console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
}
</script>
<!----------------------------------------------------------------------------------->
    <div id="content"></div>
    <script type="text/javascript" src="/static/script.js"></script>

</body>

</html>"""

class ServerIntegrationTestCase(flask_testing.LiveServerTestCase):
    
    def create_app(self):
        return app.app
        
    def test_server_sends_hello(self):
        r = requests.get(self.get_server_url())
        # self.assertEquals(r.text, 'Hello, world!')
        self.assertEquals(r.text, template)

    def test_success_status_code(self):
        r = requests.get(self.get_server_url())
        self.assertEquals(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()

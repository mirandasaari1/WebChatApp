import app, unittest, flask_testing, requests

class ServerIntegrationTestCase(
    flask_testing.LiveServerTestCase
):
    def create_app(self):
        return app.app

    def test_server_sends_hello(self):
        r = requests.get(self.get_server_url())
        self.assertEquals(r.text, 'Hello, world!')

if __name__ == '__main__':
    unittest.main()



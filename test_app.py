import unittest
import app as tested_app
import json


class FlaskAppTests(unittest.TestCase):
# TestCase is a subclass which creates a test case
    def setUp(self):
        # tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello(self):
        r = self.app.get('/')
        # self.assertEqual(r.data, b'Hello World!')
        # b means bytes not string/unicode
        # character is not a byte btw
        q = r.data.decode('UTF-8') #decode to string
        print(q)

if __name__ == '__main__':
    unittest.main()

import os
import unittest
import json
from app.app import create_app
from app.api.v1.models.UserModel import users

class UserTestCase(unittest.TestCase):
    """This class represents tests for UserView"""

    def setUp(self):
        """Define test set up"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.register = {
	                        "username":"joni",
	                        "email":"joni@gmail.com",
	                        "password":"12215",
	                        "confirm_password":"12215"
                        }
        self.login = {
                    	"username":"joni",
	                    "password":"12215"
                    }
        users.append(
            {
                "userid": 1,
                "email": "joni@gmail.com",
                "username": "joni",
                "password": "pbkdf2:sha256:50000$fq5Chau1$882cf125792fd51adc8faf974341f88dbf1b8c87f66ca4086810538cd3803eee"
            }
        )
        
    def test_register_json(self):
        response_json = self.client.post('/api/v1/register', data=json.dumps(self.register), content_type='application/json')
        self.assertEqual(response_json.status_code,201)
        self.assertIn("joni@gmail.com",str(response_json.data))

    def test_register_nonjson(self):
        response_nonjson = self.client.post('/api/v1/register', data=self.register, content_type='application/json')
        self.assertEqual(response_nonjson.status_code, 400)

    def test_register_mismatch_passwords(self):
        self.register["confirm_password"] = "545121"
        response = self.client.post('/api/v1/register', data=json.dumps(self.register), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Passwords don\\\'t match", str(response.data))

    def test_register_content_type(self):
        self.response_content = self.client.post('/api/v1/register', data=json.dumps(self.register), content_type='application/xml')
        self.assertEqual(self.response_content.status_code, 400)
        self.assertIn("POST of type Application/JSON expected",str(self.response_content.data))

    def test_login_json(self):
        response_json = self.client.post('/api/v1/login', data=json.dumps(self.login), content_type='application/json')
        self.assertEqual(response_json.status_code,200)
        self.assertIn("Successfully Logged In", str(response_json.data))

    def test_login_password(self):
        self.login["password"]="fgvjvbsjvb"
        response_json = self.client.post('/api/v1/login', data=json.dumps(self.login), content_type='application/json')
        self.assertEqual(response_json.status_code, 400)
        self.assertIn("Invalid Password", str(response_json.data))

    def test_login_username(self):
        self.login["username"] = "prinf"
        response_json = self.client.post('/api/v1/login', data=json.dumps(self.login), content_type='application/json')
        self.assertEqual(response_json.status_code, 404)
        self.assertIn("User not Found",str(response_json.data))
    
    def tearDown(self):
        users.pop()

if __name__ == "__main__":
    unittest.main()
import unittest
import json

from app.app import create_app
from app.api.v1.models.QuestionModel import questions

class AnswerTestCase(unittest.TestCase):
    '''Tests for Answer View'''

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        self.answer = {
                        "body": "Your error output lists 'connectionURI' with lowercase 'c' as invalid choice, while it also says choose from 'ConnectionURI'"+
                                 "with capital letter 'C'.Fix: Call your test with: ./argstest.py ConnectionURI oslo Maybe you should start simple (without subparsers) and build from there:",
                        "userid": '549a464020fc4e4bb0bb5f51aec9268f',
                        "votes": 2,
                        "isapproved":'false'
                    }
        questions.append(
                        {
                            'questionid':'6b49554bf5eb4a31a04ed6cf20f38ad6',
                            'title':'No Module found error',
                            'body':'I am trying to run the my flask app but i keep getting No Module found error',
                            'tags':['python3', 'flask'],
                            'userid':'9cd21d4b9215444d9dbcc70bd0d9d2b1',
                            'answered': 'false',
                            'answers':['972912aa4d5f44e0a489cb208ebb6c2d']
                        }
                    )


    def test_answer_post_ok(self):
        response = self.client.post('/api/v1/answer/6b49554bf5eb4a31a04ed6cf20f38ad6', data=json.dumps(self.answer), content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('6b49554bf5eb4a31a04ed6cf20f38ad6', str(response.data))
        self.assertEqual(type(json.loads(response.data)), dict)

    def test_answer_post_nonjson(self):
        response = self.client.post('/api/v1/answer/6b49554bf5eb4a31a04ed6cf20f38ad6', data=self.answer, content_type = 'application/xml')
        self.assertEqual(response.status_code, 400)
        self.assertIn('POST of type Application/JSON expected', str(response.data))

    def test_answer_post_notfound(self):
        response = self.client.post('/api/v1/answer/6b49554bf5eb4a31a04ed6cf20f3000g', data=json.dumps(self.answer), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Not found', str(response.data))
    
    def tearDown(self):
        questions.pop()
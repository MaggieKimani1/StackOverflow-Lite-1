import unittest
import json
from app.app import create_app
from app.api.v1.models.QuestionModel import Question, questions

class QuestionTestCase(unittest.TestCase):
    """This is Test Class for the Questions View"""
    questionid = ''
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()

        self.question = {
                            'title':'No Module found error',
                            'body':'I am trying to run the my flask app but i keep getting No Module found error',
                            'tags':['python3', 'flask']
                        }
        questions.append({
                            'questionid':'026df872f9ca443187b70c0bca04123f',
                            'title':'No Module found error',
                            'body':'I am trying to run the my flask app but i keep getting No Module found error',
                            'tags':['python3', 'flask'],
                            'userid':'9cd21d4b9215444d9dbcc70bd0d9d2b1',
                            'answered': 'false'
                        }
                    )

    def test_questions(self):
        response_json = self.client.get('/api/v1/questions')
        self.assertEqual(response_json.status_code, 200)
        self.assertEqual(type(json.loads(response_json.data)), list)

    def test_question_get_id(self):
        response_json = self.client.get('/api/v1/question/026df872f9ca443187b70c0bca04123f')
        self.assertEqual(response_json.status_code, 200)
        self.assertIn('026df872f9ca443187b70c0bca04123f', str(response_json.data))

    def test_question_get_notfound(self):
        response_json = self.client.get('/api/v1/question/026df872f9ca443187b70c0bca04000f')
        self.assertEqual(response_json.status_code, 404)
        self.assertIn('Not Found', str(response_json.data))

    def test_question_post_ok(self):
        response_json = self.client.post('/api/v1/question', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(response_json.status_code, 201)
        self.assertIn('No Module found error', str(self.question))

    def test_question_post_nonjson(self):
        response_json = self.client.post('/api/v1/question', data=self.question, content_type='application/xml')
        self.assertEqual(response_json.status_code, 400)
        self.assertIn('POST of type Application/JSON expected', str(response_json.data))

    def test_question_put_ok(self):
        question_update = questions[0]
        question_update['title'] = 'Flask Error: No Module was found'
        response_json = self.client.put('/api/v1/question/026df872f9ca443187b70c0bca04123f', data=json.dumps(question_update), content_type='application/json')
        print(response_json.data)
        self.assertEqual(response_json.status_code, 202)
        response_data = json.loads(response_json.data)
        self.assertEqual(response_data['title'], question_update['title'])
    
    def test_question_put_nonjson(self):
        question_update = questions[0]
        question_update['title'] = 'Flask Error: No Module was found'
        response_json = self.client.put('/api/v1/question/026df872f9ca443187b70c0bca04123f', data=question_update, content_type='application/xml')
        self.assertEqual(response_json.status_code, 400)
        self.assertIn('POST of type Application/JSON expected', str(response_json.data))
         
    def test_question_put_notfound(self):
        question_update = questions[0]
        question_update['title'] = 'Flask Error: No Module was found'
        response_json = self.client.put('/api/v1/question/026df872f9ca443187b70c0bca04000t', data=json.dumps(question_update), content_type='application/json')
        print(response_json.data)
        self.assertEqual(response_json.status_code, 404)
        self.assertIn('Not Found', str(response_json.data))

    def test_question_delete_ok(self):
        response_json = self.client.delete('/api/v1/question/026df872f9ca443187b70c0bca04123f')
        self.assertEqual(response_json.status_code, 204)

    def test_question_delete_notfound(self):
        response_json = self.client.delete('/api/v1/question/026df872f9ca443187b70c0bca04000t')
        self.assertEqual(response_json.status_code, 404)
        self.assertIn('Not found', str(response_json.data))

    def test_user_questions_ok(self):
        response_json = self.client.get('/api/v1/userquestions/9cd21d4b9215444d9dbcc70bd0d9d2b1')
        self.assertEqual(response_json.status_code,200)
        self.assertEqual(type(json.loads(response_json.data)),list)
    
    def tearDown(self):
        questions.pop()

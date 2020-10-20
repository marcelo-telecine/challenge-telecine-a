from main.routes import api
from main.app import app
from bson import ObjectId

import unittest



class TestSources(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = app.test_client()
        self.payload = {'its': 'empty'}

    def tearDown(self):
        pass

    def test_get_api(self):
        self.RESOURCE_URL = "/api/v1/"
        response = self.client.get(self.RESOURCE_URL, json={})
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), {'up': True})

if __name__ == '__main__':
    unittest.main()
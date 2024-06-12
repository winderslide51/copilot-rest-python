from rest_framework.test import APITestCase
from rest_framework.utils import json

class TimeAPITestCase(APITestCase):
    api_path = '/api/time/'

    def test_get_current_time(self):
        response = self.client.get(self.api_path)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertIn('time', response_data)
        self.assertIsNotNone(response_data['time'])

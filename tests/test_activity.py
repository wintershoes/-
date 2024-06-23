# editor : banyanrong
# time : 2024/6/23 16:40
import unittest
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.model import Activity
from datetime import date


class ActivityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_add_activity(self):
        response = self.client.post('/api/activities', json={
            'name': 'Test Activity',
            'description': 'This is a test activity',
            'start_time': date.today(),
            'end_time': date.today(),
            'location': 'Test Location',
            'link': 'http://testlink.com'
        })
        self.assertEqual(response.status_code, 201)
    #
    # def test_get_activity(self):
    #     self.client.post('/api/activities', json={
    #         'name': 'Test Activity',
    #         'description': 'This is a test activity',
    #         'start_time': date.today(),
    #         'end_time': date.today(),
    #         'location': 'Test Location',
    #         'link': 'http://testlink.com'
    #     })
    #     response = self.client.get('/api/activities/1')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('Test Activity', response.get_data(as_text=True))
    #
    # def test_get_all_activities(self):
    #     self.client.post('/api/activities', json={
    #         'name': 'Test Activity 1',
    #         'description': 'This is a test activity 1',
    #         'start_time': date.today(),
    #         'end_time': date.today(),
    #         'location': 'Test Location 1',
    #         'link': 'http://testlink1.com'
    #     })
    #     self.client.post('/api/activities', json={
    #         'name': 'Test Activity 2',
    #         'description': 'This is a test activity 2',
    #         'start_time': date.today(),
    #         'end_time': date.today(),
    #         'location': 'Test Location 2',
    #         'link': 'http://testlink2.com'
    #     })
    #     response = self.client.get('/api/activities')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.json), 2)
    #
    # def test_update_activity(self):
    #     self.client.post('/api/activities', json={
    #         'name': 'Test Activity',
    #         'description': 'This is a test activity',
    #         'start_time': date.today(),
    #         'end_time': date.today(),
    #         'location': 'Test Location',
    #         'link': 'http://testlink.com'
    #     })
    #     response = self.client.put('/api/activities/1', json={
    #         'name': 'Updated Activity',
    #         'description': 'This is an updated test activity',
    #         'start_time': date.today(),
    #         'end_time': date.today(),
    #         'location': 'Updated Location',
    #         'link': 'http://updatedlink.com'
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('Updated Activity', response.get_data(as_text=True))
    #
    # def test_delete_activity(self):
    #     self.client.post('/api/activities', json={
    #         'name': 'Test Activity',
    #         'description': 'This is a test activity',
    #         'start_time': date.today(),
    #         'end_time': date.today(),
    #         'location': 'Test Location',
    #         'link': 'http://testlink.com'
    #     })
    #     response = self.client.delete('/api/activities/1')
    #     self.assertEqual(response.status_code, 200)
    #     response = self.client.get('/api/activities/1')
    #     self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

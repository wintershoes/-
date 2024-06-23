# editor : banyanrong
# time : 2024/6/23 16:40
import unittest
from app import create_app, db
from app.models.models import Activity
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
            'start_time': date.today().isoformat(),
            'end_time': date.today().isoformat(),
            'location': 'Test Location',
            'link': 'http://testlink.com',
            'authorization': "admin"
        })
        self.assertEqual(response.status_code, 201)

    def test_get_activity(self):
        response = self.client.post('/api/activities', json={
            'name': 'Test Activity',
            'description': 'This is a test activity',
            'start_time': date.today().isoformat(),
            'end_time': date.today().isoformat(),
            'location': 'Test Location',
            'link': 'http://testlink.com',
            'authorization': "admin"
        })
        activity_id = response.json['activityId']
        response = self.client.get(f'/api/activities/{activity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Activity', response.get_data(as_text=True))

    def test_get_all_activities(self):
        self.client.post('/api/activities', json={
            'name': 'Test Activity 1',
            'description': 'This is a test activity 1',
            'start_time': date.today().isoformat(),
            'end_time': date.today().isoformat(),
            'location': 'Test Location 1',
            'link': 'http://testlink1.com',
            'authorization': 'admin'
        })
        self.client.post('/api/activities', json={
            'name': 'Test Activity 2',
            'description': 'This is a test activity 2',
            'start_time': date.today().isoformat(),
            'end_time': date.today().isoformat(),
            'location': 'Test Location 2',
            'link': 'http://testlink2.com',
            'admin': 'authorization'
        })
        response = self.client.get('/api/activities')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 2)

    def test_update_activity(self):
        response = self.client.post('/api/activities', json={
            'name': 'Test Activity',
            'description': 'This is a test activity',
            'start_time': date.today().isoformat(),
            'end_time': date.today().isoformat(),
            'location': 'Test Location',
            'link': 'http://testlink.com',
            'authorization': 'admin'
        })
        activity_id = response.json["activityId"]
        response = self.client.put(f'/api/activities/{activity_id}', json={
            'name': 'Updated Activity',
            'description': 'This is an updated test activity',
            'start_time': date.today().isoformat(),
            'end_time': date.today().isoformat(),
            'location': 'Updated Location',
            'link': 'http://updatedlink.com',
            'authorization': 'admin'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Activity information updated successfully")

    def test_delete_activity(self):
        response = self.client.post('/api/activities', json={
            'name': 'Test Activity',
            'description': 'This is a test activity',
            'start_time': date.today().isoformat(),
            'end_time': date.today().isoformat(),
            'location': 'Test Location',
            'link': 'http://testlink.com',
            'authorization': 'admin'
        })
        activity_id = response.json["activityId"]
        response = self.client.delete(f'/api/activities/{activity_id}', json={
            "authorization": 'admin'
        })
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f'/api/activities/{activity_id}', json={
            "authorization": 'admin'
        })
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

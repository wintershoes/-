import unittest
from app import create_app, db
from app.models.models import User, Book, Reservation
from datetime import date


class ReservationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            user = User(username='testuser', password="123456", email="123@163.com", role="admin", points=100000000000)
            pos_user = User(username='testuser', password="123456", email="123@163.com", role="admin", points=0)
            book = Book(title='testbook', author="test", publisher="testor", publish_date=date.today(), isbn="123456", location="west", status="available")
            db.session.add(user)
            db.session.add(book)
            db.session.add(pos_user)
            db.session.commit()
            self.user_id = user.user_id
            self.book_id = book.book_id
            self.pos_user_id = pos_user.user_id

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_add_reservation(self):
        response = self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'confirmed',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        self.assertEqual(response.status_code, 201)
        # response = self.client.post('/api/reservations', json={
        #     'user_id': self.user_id,
        #     'book_id': self.book_id,
        #     'status': 'confirmed',
        #     'book_location': 'Library',
        #     'reservation_location': 'Online',
        #     'authorization': 'student'
        # })
        # self.assertEqual(response.status_code, 404)

    def test_get_reservation(self):
        response = self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'confirmed',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'admin'
        })
        reservation_id = response.json['reservationId']
        response = self.client.get(f'/api/reservations/{reservation_id}', json={
            'authorization': 'student'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('confirmed', response.get_data(as_text=True))

    def test_get_all_confirmed_reservations(self):
        self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'confirmed',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'cancelled',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        response = self.client.get('/api/reservations/confirmed', json={
            'authorization': "student"
        })
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json), 1)

    def test_get_reservation_by_user(self):
        self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'confirmed',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'cancelled',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        response = self.client.get(f'/api/reservations/user/{self.user_id}', json={
            'authorization': "student"
        })
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json), 1)

    def test_get_reservation_by_book(self):
        self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'confirmed',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'cancelled',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        response = self.client.get(f'/api/reservations/book/{self.book_id}', json={
            'authorization': "student"
        })
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json), 1)

    def test_cancel_reservation(self):
        response = self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'confirmed',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        reservation_id = response.json["reservationId"]
        response = self.client.put(f'/api/reservations/{reservation_id}/cancel', json={
            'authorization': "student"
        })
        self.assertEqual(response.status_code, 200)

    def test_update_reservation(self):
        response = self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'confirmed',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        reservation_id = response.json["reservationId"]
        response = self.client.put(f'/api/reservations/{reservation_id}', json={
            'status': 'completed',
            'book_location': 'Library',
            'reservation_location': 'Onsite',
            'authorization': 'admin'
        })
        self.assertEqual(response.status_code, 200)

    def test_complete_reservation(self):
        response = self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'confirmed',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        reservation_id = response.json["reservationId"]
        response = self.client.put(f'/api/reservations/{reservation_id}/complete', json={
            'user_id': self.pos_user_id,
            'authorization': 'admin'
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_reservation(self):
        response = self.client.post('/api/reservations', json={
            'user_id': self.user_id,
            'book_id': self.book_id,
            'status': 'confirmed',
            'book_location': 'Library',
            'reservation_location': 'Online',
            'authorization': 'student'
        })
        reservation_id = response.json["reservationId"]
        response = self.client.delete(f'/api/reservations/{reservation_id}', json={
            'authorization': 'admin'
        })
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f'/api/reservations/{reservation_id}', json={
            'authorization': 'admin'
        })
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Traveller, Venue, db


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.VIEWER = os.environ['VIEWER']
        self.COADMIN = os.environ['COADMIN']
        self.ADMIN = os.environ['ADMIN']

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)
        self.database_host = '127.0.0.1:5432'
        self.database_username = 'postgres'
        self.database_name = 'capstone'
        self.database_path = 'postgresql+psycopg2://{}@{}/{}'.format(
            self.database_username,
            self.database_host,
            self.database_name)
        setup_db(self.app, self.database_path)

        self.new_traveller = {
            "name": "William",
            "age": 32,
            "gender": "male"
        }

        self.new_venue = {
            "vname": "Dr Strange",
            "duration": 3,
            "visit_year": 2016
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            self.db.create_all()

    def tearDown(self):
        pass

    def test_health(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], 'done the FSND!!')

    def test_get_travellers_without_token(self):
        res = self.client().get('/travellers')
        self.assertEqual(res.status_code, 401)
        

    def test_get_travellers_with_valid_token(self):
        res = self.client().get(
            '/travellers',
            headers={
                "Authorization": f"Bearer {self.ADMIN}"})
        self.assertEqual(res.status_code, 200)

    def test_get_specific_traveller_without_token(self):
        res = self.client().get('/travellers/8')
        self.assertEqual(res.status_code, 401)

    def test_get_specific_traveller_with_valid_token(self):
        res = self.client().get(
            '/travellers/8',
            headers={
                "Authorization": f"Bearer {self.ADMIN}"})
        self.assertEqual(res.status_code, 200)

    def test_create_traveller_without_token(self):
        res = self.client().post('/travellers', json=self.new_traveller)
        self.assertEqual(res.status_code, 401)

    def test_create_traveller_with_valid_token(self):
        res = self.client().post(
            '/travellers',
            headers={
                "Authorization": f"Bearer {self.ADMIN}"},
            json=self.new_traveller)
        self.assertEqual(res.status_code, 200)

    def test_patch_traveller_without_token(self):
        res = self.client().patch('/travellers/8', json=self.new_traveller)
        self.assertEqual(res.status_code, 401)

    def test_patch_traveller_with_valid_token(self):
        res = self.client().patch(
            '/travellers/8',
            headers={
                "Authorization": f"Bearer {self.ADMIN}"},
            json=self.new_traveller)
        self.assertEqual(res.status_code, 200)

    def test_delete_traveller_without_token(self):
        res = self.client().delete('/travellers/10')
        self.assertEqual(res.status_code, 401)

    def test_delete_traveller_with_valid_token(self):
        res = self.client().delete('/travellers/10',
                                   headers={"Authorization": f"Bearer {self.ADMIN}"})
        self.assertEqual(res.status_code, 200)
    # TESTS FOR venueS

    def test_get_venues_without_token(self):
        res = self.client().get('/venues')
        self.assertEqual(res.status_code, 401)

    def test_get_venues_with_valid_token(self):
        res = self.client().get(
            '/venues',
            headers={
                "Authorization": f"Bearer {self.ADMIN}"})
        self.assertEqual(res.status_code, 200)

    def test_get_specific_venue_without_token(self):
        res = self.client().get('/venues/6')
        self.assertEqual(res.status_code, 401)

    def test_get_specific_venue_with_valid_token(self):
        res = self.client().get(
            '/venues/6',
            headers={
                "Authorization": f"Bearer {self.ADMIN}"})
        self.assertEqual(res.status_code, 200)

    def test_create_venue_without_token(self):
        res = self.client().post('/venues', json=self.new_venue)
        self.assertEqual(res.status_code, 401)

    def test_create_venue_with_valid_token(self):
        res = self.client().post(
            '/venues',
            headers={
                "Authorization": f"Bearer {self.ADMIN}"},
            json=self.new_venue)
        self.assertEqual(res.status_code, 200)

    def test_patch_venue_without_token(self):
        res = self.client().patch('/venues/6', json=self.new_venue)
        self.assertEqual(res.status_code, 401)

    def test_patch_venue_with_valid_token(self):
        res = self.client().patch(
            '/venues/6',
            headers={
                "Authorization": f"Bearer {self.ADMIN}"},
            json=self.new_venue)
        self.assertEqual(res.status_code, 200)

    def test_delete_venue_without_token(self):
        res = self.client().delete('/venues/8')
        self.assertEqual(res.status_code, 401)

    def test_delete_venue_with_valid_token(self):
        res = self.client().delete('/venues/8',
                                   headers={"Authorization": f"Bearer {self.ADMIN}"})
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()

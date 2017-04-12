import unittest
import json

from run import app, db
from models import Furniture


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app_context().push()
        self.client = app.test_client()
        db.create_all()

    def test_add_furniture(self):
        new_furniture = {
            "furniture_type": "SOFA",
            "price": 120000
        }
        response = self.client.post("/furniture", data=json.dumps(new_furniture))
        self.assertEqual(response.status_code, 201)


    def test_add_furniture_with_no_price(self):
        new_furniture = {
            "furniture_type": "SOFA"
        }
        response = self.client.post("/furniture", data=json.dumps(new_furniture))
        self.assertEqual(response.status_code, 400)

    def test_view_furniture(self):
        response = self.client.get("/furniture")
        self.assertEqual(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()
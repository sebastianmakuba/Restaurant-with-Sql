import sys
import os
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from models.restaurant import Restaurant
from models.base import Base

class TestRestaurant(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        # Create tables in an in-memory SQLite database
        Base.metadata.create_all(engine)

    def test_create_restaurant(self):
        restaurant = Restaurant("Tasty Bites")
        self.session.add(restaurant)
        self.session.commit()

        retrieved_restaurant = self.session.query(Restaurant).first()
        self.assertEqual(retrieved_restaurant.get_name(), "Tasty Bites")


if __name__ == '__main__':
    unittest.main()

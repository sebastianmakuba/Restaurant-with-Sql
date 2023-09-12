import sys
import os
import unittest
from sqlalchemy import create_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.restaurant import Restaurant
from models.review import Review
from models.customer import Customer




class TestReview(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        # Create tables in an in-memory SQLite database
        Base.metadata.create_all(engine)

    def test_create_review(self):
        customer = Customer("John", "Doe")
        restaurant = Restaurant("Tasty Bites")
        review = Review(customer, restaurant, 4.5)

        self.session.add_all([customer, restaurant, review])
        self.session.commit()

        retrieved_review = self.session.query(Review).first()
        self.assertEqual(retrieved_review.rating, 4.5)


if __name__ == '__main__':
    unittest.main()

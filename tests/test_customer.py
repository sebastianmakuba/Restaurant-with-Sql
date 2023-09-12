import sys
import os
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.customer import Customer
from models.base import Base

class TestCustomer(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        # Create tables in an in-memory SQLite database
        Base.metadata.create_all(engine)

    def test_create_customer(self):
        customer = Customer("John", "Doe")
        self.session.add(customer)
        self.session.commit()

        retrieved_customer = self.session.query(Customer).first()
        self.assertEqual(retrieved_customer.get_full_name(), "John Doe")

    

if __name__ == '__main__':
    unittest.main()

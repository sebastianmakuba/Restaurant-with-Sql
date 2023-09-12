# customer.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.review import Review

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    reviews = relationship('Review', back_populates='customer')

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def get_full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls, session):
        return session.query(cls).all()

    def get_restaurants(self, session):
        return list({review.restaurant for review in self.reviews})

    def add_review(self, session, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        session.add(new_review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, session, full_name):
        given_name, family_name = full_name.split()
        return session.query(cls).filter_by(given_name=given_name, family_name=family_name).first()

    @classmethod
    def find_all_by_given_name(cls, session, given_name):
        return session.query(cls).filter_by(given_name=given_name).all()

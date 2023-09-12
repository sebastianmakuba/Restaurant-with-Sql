# restaurant.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from models.base import Base
from models.review import Review

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    reviews = relationship('Review', back_populates='restaurant')

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_reviews(self, session):
        return session.query(Review).filter(Review.restaurant == self).all()

    def get_customers(self, session):
        return list({review.customer for review in self.reviews})

    def average_star_rating(self, session):
        ratings = [review.rating for review in self.reviews]
        if ratings:
            return sum(ratings) / len(ratings)
        return 0

    @classmethod  
    def all(cls, session):
        return session.query(cls).all()
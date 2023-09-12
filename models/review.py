
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Float)

    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    customer = relationship('Customer', back_populates='reviews')

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def rating(self):
        return self.rating

    @classmethod
    def all(cls, session):
        return session.query(cls).all()

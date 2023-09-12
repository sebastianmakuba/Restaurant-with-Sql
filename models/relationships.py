from sqlalchemy.orm import relationship
from review import Review
from customer import Customer
from restaurant import Restaurant

# Defining relationships

Review.customer = relationship(Customer, back_populates='review')
Review.restaurant = relationship(Restaurant, back_populates='review')
Customer.reviews = relationship(Review, back_populates='customer')
Restaurant.reviews = relationship(Review, back_populates='restaurant')


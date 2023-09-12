from sqlalchemy.orm import relationship
from review import Review
from customer import Customer
from restaurant import Restaurant

# Defining relationships

Review.customer = relationship(Customer, back_populates='reviews')
Review.restaurant = relationship(Restaurant, back_populates='review_relationship')
Customer.reviews = relationship(Review, back_populates='customer')
Restaurant.review_relationship = relationship(Review, back_populates='restaurant')


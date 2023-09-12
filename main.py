
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review
from models.base import Base

engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine) 

customer1 = Customer("John", "Doe")
customer2 = Customer("Alice", "Smith")

restaurant1 = Restaurant("Tasty Bites")
restaurant2 = Restaurant("Pizza Palace")

customer1.add_review(session, restaurant1, 4.5)
customer1.add_review(session, restaurant2, 3.8)
customer2.add_review(session, restaurant1, 4.2)

all_customers = Customer.all(session)
all_restaurants = Restaurant.all(session)
all_reviews = Review.all(session)

print("All Customers:")
for customer in all_customers:
    print(customer.get_full_name())

print("\nAll Restaurants:")
for restaurant in all_restaurants:
    print(restaurant.get_name())

print("\nAll Reviews:")
for review in all_reviews:
    print(f"Customer: {review.customer.get_full_name()}, Restaurant: {review.restaurant.get_name()}, Rating: {review.rating}")

found_customer = Customer.find_by_name(session, "John Doe")
if found_customer:
    print(f"\nFound Customer: {found_customer.get_full_name()}")

customers_with_given_name = Customer.find_all_by_given_name(session, "Alice")
if customers_with_given_name:
    print("\nCustomers with Given Name 'Alice':")
    for customer in customers_with_given_name:
        print(customer.get_full_name())

avg_rating = restaurant1.average_star_rating(session)
print(f"\nAverage Star Rating for '{restaurant1.get_name()}': {avg_rating}")

customer1_restaurants = customer1.get_restaurants(session)
print(f"\nUnique Restaurants Reviewed by {customer1.get_full_name()}:")
for restaurant in customer1_restaurants:
    print(restaurant.get_name())

session.commit()

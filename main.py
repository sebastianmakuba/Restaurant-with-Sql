from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review


engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create instances of Customer and Restaurant
customer1 = Customer("John", "Doe")
customer2 = Customer("Alice", "Smith")

restaurant1 = Restaurant("Tasty Bites")
restaurant2 = Restaurant("Pizza Palace")

# Add reviews
customer1.add_review(session, restaurant1, 4.5)
customer1.add_review(session, restaurant2, 3.8)
customer2.add_review(session, restaurant1, 4.2)

# Retrieve all customers, restaurants, and reviews
all_customers = Customer.all(session)
all_restaurants = Restaurant.all(session)
all_reviews = Review.all(session)

print("All Customers:")
for customer in all_customers:
    print(customer.full_name())

print("\nAll Restaurants:")
for restaurant in all_restaurants:
    print(restaurant.name)

print("\nAll Reviews:")
for review in all_reviews:
    print(f"Customer: {review.customer.full_name()}, Restaurant: {review.restaurant.name}, Rating: {review.rating}")

# Find a customer by name
found_customer = Customer.find_by_name(session, "John Doe")
if found_customer:
    print(f"\nFound Customer: {found_customer.full_name()}")

# Find all customers by given name
customers_with_given_name = Customer.find_all_by_given_name(session, "Alice")
if customers_with_given_name:
    print("\nCustomers with Given Name 'Alice':")
    for customer in customers_with_given_name:
        print(customer.full_name())

# Calculate average star rating for a restaurant
avg_rating = restaurant1.average_star_rating(session)
print(f"\nAverage Star Rating for '{restaurant1.name}': {avg_rating}")

# Retrieve unique restaurants a customer has reviewed
customer1_restaurants = customer1.restaurants(session)
print(f"\nUnique Restaurants Reviewed by {customer1.full_name()}:")
for restaurant in customer1_restaurants:
    print(restaurant.name)

# Commit changes to the database
session.commit()

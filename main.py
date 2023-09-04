from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.restaurant import Restaurant
from models.review import Review
from models.customer import Customer

# Set up your SQLAlchemy session and database engine
engine = create_engine('sqlite:///your_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main():
    # Create instances and perform operations as needed
    new_restaurant = Restaurant(name="Sample Restaurant", price=3)
    new_customer = Customer(first_name="John", last_name="Doe")

    # Add a review by the customer for the restaurant
    new_customer.add_review(new_restaurant, 5)

    # Query and test your methods
    sample_customer = session.query(Customer).first()
    sample_restaurant = session.query(Restaurant).first()

    print(sample_customer.reviews())  
    print(sample_customer.restaurants())  
    print(sample_customer.favorite_restaurant().name)  
    print(sample_customer.full_name())  
    print(sample_restaurant.reviews())  
    print(sample_restaurant.customers())  
    print(sample_restaurant.fanciest().name)  
    print(sample_restaurant.all_reviews())  

if __name__ == "__main__":
    main()

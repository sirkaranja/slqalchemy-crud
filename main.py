from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker

# Create the database engine
engine = create_engine('sqlite:///food.db', echo=True)

# Create the base class for declarative models
Base = declarative_base()

# Define the Food class as a subclass of Base
class Food(Base):
    __tablename__ = 'foods'  # Name of the table in the database

    # Define the columns of the table
    id = Column(Integer, primary_key=True)
    foodname = Column(String(50))
    price = Column(Float)

# Create a session factory bound to the engine
Session = sessionmaker(bind=engine)

# Create the table(s) in the database if they don't exist
Base.metadata.create_all(engine)

# Function to create a new food record
def create_food(foodname, price):
    session = Session()  # Open a new session
    food = Food(foodname=foodname, price=price)  # Create a new Food object
    session.add(food)  # Add the object to the session
    session.commit()  # Commit the changes to the database
    session.close()  # Close the session
    print("Food created successfully.")

# Function to read all food records
def read_foods():
    session = Session()  # Open a new session
    foods = session.query(Food).all()  # Query all food records from the database
    for food in foods:
        print(f"ID: {food.id}, Food Name: {food.foodname}, Price: {food.price}")
    session.close()  # Close the session

# Function to update a food record
def update_food(food_id, new_foodname, new_price):
    session = Session()  # Open a new session
    food = session.query(Food).filter_by(id=food_id).first()  # Query the food record to update
    if food:
        food.foodname = new_foodname  # Update the food name
        food.price = new_price  # Update the price
        session.commit()  # Commit the changes to the database
        print("Food updated successfully.")
    else:
        print("Food not found.")
    session.close()  # Close the session

# Function to delete a food record
def delete_food(food_id):
    session = Session()  # Open a new session
    food = session.query(Food).filter_by(id=food_id).first()  # Query the food record to delete
    if food:
        session.delete(food)  # Delete the food record
        session.commit()  # Commit the changes to the database
        print("Food deleted successfully.")
    else:
        print("Food not found.")
    session.close()  # Close the session

# Create a new food
#create_food('Pilau', 350.0)

# Read all foods
read_foods()

# # Update a food
update_food(3, 'Biryani', 700.0)

# # Delete a food
# delete_food(6)
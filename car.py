import random
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.mileage = random.randint(1000, 50000)

    def describe(self):
        return f"This is a {self.brand} {self.model} car, with {self.mileage} miles on it."

brand_input = input("Enter your car brand here: ")
model_input = input("Enter your car model here: ")

my_car = Car(brand_input, model_input)
print(my_car.describe())


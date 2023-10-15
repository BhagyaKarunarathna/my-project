import random
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.mileage = random.randint(1000, 50000)

    def describe(self):
        return f"This is a {self.year} {self.color} {self.brand} {self.model} car, with {self.mileage} miles on it."


brand_input = input("Enter your car brand here: ")
model_input = input("Enter your car model here: ")
year_input = input("Enter the car's year: ")
color_input = input("Enter the car's color: ")

my_car = Car(brand_input, model_input, year_input, color_input)
print(my_car.describe())


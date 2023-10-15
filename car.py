class Car:
    name = ""
    def __init__(self, brand):
        self.brand = brand
        self.mileage = 0

    def describe(self):
        return f"This is a {self.brand} car, with {self.mileage} miles on it."

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"This is a {self.year} {self.make} {self.model}"

    def is_a_recent_car(self):
        return self.year > 2014

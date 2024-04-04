class Car:
    def __init__(self, make, model):
        self.public_make = make
        self._protected_model = model
        self.__private_year = 2022

    def public_method(self):
        return f"It is a public method. Car:{self.public_make} {self._protected_model}"

    def _protected_method(self):
        return f"It is a protected method. "

    def __private_method(self):
        return f"It is a private method. "


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        details = f"Car: {self.public_make} {self._protected_model} Battery size: {self.battery_size} KWh"
        return details

tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.public_make)
print(tesla.public_method())

print(tesla._protected_model)
print(tesla._protected_method())

print(tesla._Car__private_year)

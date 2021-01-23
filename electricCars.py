# Importing a module into a module.
# We do this if we are dealing with very large files and we want to spread our modules out so they are easier to manage.
# Because the Classes Battery and ElectricCar need our original Car class, we need to import the Class Car from cars.py so they can use the parent class.

"""A set of classes that can be used to represent electric cars."""
from cars import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, batterySize=75):
        """Init the battery's attributes."""
        self.batterySize = batterySize

    def describeBattery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.batterySize}-kWh battery.")

    def getRange(self):
        """Print a statement about the range this battery provides."""
        if self.batterySize == 75:
            range = 260
        elif self.batterySize == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgradeBattery(self):
        if self.batterySize == 75:
            self.batterySize = 100
        else:
            print("Your battery is already the max size offered.")

class ElectricCar(Car):

    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

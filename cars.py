# A module for a car (from car.py)
# We should include a docstring at the module level (global) that briefly describes the content

"""A class that can be used to represent a car"""
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Init attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometerReading} miles on it.")

    def updateOdometer(self, mileage):
        """Set the odometer reading to the given value"""
        """Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    # We create a new method that takes in a number of miles and adds this
    # value to self.odometerReading
    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        # Doing some self coding to reject negative miles
        if miles >= 0:
            self.odometerReading += miles
        else:
            print("You can't have negative miles...")

# Adding the below for myElectricCar.py (storing multiple classes)
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

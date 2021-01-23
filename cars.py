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

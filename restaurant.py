"""A class for simulating restaurants"""

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
# Make a separate file that imports Restaurant. Make a Restaurant instance,
# and call one of Restaurant’s methods to show that the import statement is working
# properly.

# see dog.py for import

class Restaurant:
    def __init__(self, restaurantName, cuisineType):
        """Init attr for restaurant name and cuisine"""
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType

    def describeRestaurant(self):
        """Describing the restaurant"""
        print(
            f"The restaurant is called {self.restaurantName} and it serves {self.cuisineType.title()}.")

    def openRestaurant(self):
        """Simulating opening of restaurant"""
        print(f"{self.restaurantName.title()} is now open!")

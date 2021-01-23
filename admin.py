"""Admin portion of user class"""

# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.

# Need to import User class from user.py as the classes below are it's children
from users import User

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def showPrivileges(self):
        print("\nThe admin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Admin(User):
    """Modeling a special user"""

    def __init__(self, firstName, lastName, age, nationality):
        super().__init__(firstName, lastName, age, nationality)
        self.privileges = Privileges()

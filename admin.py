# 9-11

class User():
    """A class describing an user."""
    
    def __init__(self, first_name, last_name, age, sex, membership):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.membership = membership
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints the user information."""
        print("\n" + self.first_name.title() + " " + self.last_name.title())
        print(" Age: " + str(self.age))
        print(" Sex: " + self.sex)
        print(" Membership: " + self.membership)
        
    def greet_user(self):
        """Greets the user personalized."""
        msg = "\nHello " + self.first_name.title() + " " + self.last_name.title() +"!" + "\nHow are you?"
        print(msg)
        
    def read_login_attempts(self):
        """Shows the login attempts."""
        print("The User: " + self.first_name.title() + " has " + str(self.login_attempts) + " login attempts.")
    
    def increment_login_attempts(self, update):
        """Increments the login attempts. The initial value is 0!"""
        self.login_attempts += update
        
    def reset_login_attempts(self):
        """Resets the login attempts to 0 again."""
        self.login_attempts = 0
        
        
class Admin(User):
    """A class describing the Admin, which is also a user!"""
    
    def __init__(self, first_name, last_name, age, sex, membership):
        """Initialize attributes of the parent class.
        Then initialize attributes specific."""
        super().__init__(first_name, last_name, age, sex, membership)
        
        self.privileges = Privileges()
            
class Privileges():
    """A class for privileges."""
   
    def __init__(self, privileges=[]):
        self.privileges = privileges

    
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- No privileges.")
            
ugur = Admin('ugur', 'tigu', 30, 'male', 'gold')
ugur.describe_user()

ugur.privileges.show_privileges()

print("\nAdding priviliges...")
ugur_privileges = [
    'can add',
    'can delete',
    'can edit',
]

ugur.privileges.privileges = ugur_privileges
ugur.privileges.show_privileges()

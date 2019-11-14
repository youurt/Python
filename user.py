
# 9-12

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

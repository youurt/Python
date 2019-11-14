
class Admin(User):
    """A class describing the Admin, which is also a user!"""
    
    def __init__(self, first_name, last_name, age, sex, membership):
        """Initialize attributes of the parent class.
        Then initialize attributes specific."""
        super().__init__(first_name, last_name, age, sex, membership)
        
        self.privileges = Privileges()

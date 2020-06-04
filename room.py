class Room:
    def __init__(self, name, description): 
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

   
    def __getattr__(self, name):
        """
        Defaults to None for any attribute not in the class currently
        """
        return None

    def __str__(self):
        """
        Replacement string method for the Room class
        """
        return f"Name: {self.name}, Description: {self.description}"

    def __repr__(self):
        """
        REPR method for the Room class
        """
        return f"Room({repr(self.name)}, {repr(self.description)})"
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name):
        """
        This is constructor function creates all needed variables for instantiation of a new player
        """
        self.current_room = "outside"
        self.name = name

    def set_room(self, current_room):
        """
        This method sets the new room for the player as they move throughout the game
        """
        self.current_room = current_room



    def __getattr__(self, name):
        """
        Defaults to None for any attribute not in the class currently
        """
        return None

    def __str__(self):
        """
        Replacement string method for the Player class
        """
        return f"Name: {self.name}, Room: {self.room}."

    def __repr__(self):
        """
        REPR method for the Player class
        """
        return f"Player({repr(self.name)}"
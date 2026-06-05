class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        """Constructor with default values."""
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # Speed
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed

    # Radius
    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    # Color
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    # On / Off status
    def is_on(self):
        return self.__on

    def set_on(self, on):
        self.__on = on

    def __str__(self):
        """Helper method to easily display fan properties."""
        return (f"Speed: {self.__speed}, "
                f"Radius: {self.__radius}, "
                f"Color: {self.__color}, "
                f"On: {self.__on}")
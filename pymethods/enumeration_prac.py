from enum import Enum

#The class color is an enumeration
#attributes Color.RED, Color.GREEN, and Color.BLUE are enumeration members and functionaly constants
#The enum members have names and values (The name of Color.RED is RED and the value of Color.BLUE is 3)
#Enum is the base class for enumerated constants
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])
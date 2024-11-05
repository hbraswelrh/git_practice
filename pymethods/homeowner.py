#This is a class that has a defined name, rooms, and stories tht includes a static method that only applies to the method home
#The method home runs the implicit function and is a method that is statically defined and evaluates the boolean function
#static method will evaluate with any call that uses the home method
#boolean true or false for if the home name is empty, otherwise the home is not on the market
#The wall paint is a class method that only is applied to the class
#the paint_wall is specifically linked to the home class


class Home:
    name="Code Ninja"
    rooms = 4
    stories = 2

    @staticmethod
    def is_on_market(home):
        if(home.name == ""):
            return True
        else:
            return False
        
    @classmethod
    def paint_wall(self, color):
        return f"Painting wall with the color {color}."
        
    home = Home()
    print(Home.is_on_market(home))
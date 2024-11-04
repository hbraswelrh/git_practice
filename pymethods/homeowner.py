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
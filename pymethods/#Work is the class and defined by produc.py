#Work is the class and defined by productivity variable
#The being_productive() method is defined in the Work class body
#The being_productive() method takes a parameter codeacademy and uses it to validate statement
#If being productive, change to unproductive because of resource usage codeacademy
#Otherwise print the productivity message

#the laptop instance calls the class as a function and uses is_productive ad runs the being_productive() method until printing
class Work:

    is_productive = False

    def being_productive(self, codeacademy):
        if(self.is_productive):
            self.is_productive = True
            print(f"Learning with {codeacademy}. Brain stimulated.")
        else:
            print("Not being productive.")

            laptop = Work()
            laptop.being_productive('python')
            laptop.being_productive('go language')
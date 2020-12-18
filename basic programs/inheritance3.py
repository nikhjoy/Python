class BaseClass:
    def __init__(self):
        print("base class init")

    def set_name(self,name):
        self.name = name
        print("base class set name")

class SubClass(BaseClass):

    def __init__(self):
        #BaseClass.__init__(self)
        super().__init__()
        print("subclass init")

    def set_name(self,name):
        super().set_name(name)
        print("sub class set name")

    def welcome(self):
        print("melcow")

    def display_name(self):
        print("Name: "+self.name)


y = SubClass()
y.welcome()
y.set_name("dilshad")
y.display_name()
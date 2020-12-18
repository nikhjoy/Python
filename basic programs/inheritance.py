class BaseClass:
    def display(self):
        print("hello")

class SubClass(BaseClass):
    def welcome(self):
        print("melcow")

x = BaseClass()
x.display()

y = SubClass()
y.display()
y.welcome()
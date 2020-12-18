class First:
    def displayFirst(self):
        print("first")

class Second:
    def displaySecond(self):
        print("Second")

class Third(First,Second):
    def displaythird(self):
        print("third")

x = Third()
x.displaythird()
x.displayFirst()
x.displaySecond()
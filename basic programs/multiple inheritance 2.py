class First:
    def display(self):
        print("first")


class Second:
    def display(self):
        print("Second")


class Third(Second,First):
    def display(self):
        print("third")


x = Third()
#x.displaythird()
x.display()

print(Third.mro())

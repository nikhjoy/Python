class First:
    def display_first(self):
        print("first")


class Second(First):
    def display_second(self):
        print("Second")


class Third(Second):
    def display_third(self):
        print("third")


x = Third()
x.display_third()
x.display_first()

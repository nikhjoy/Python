class CrossroadsTeamMember:
    year = 2020

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Year: " + str(CrossroadsTeamMember.year))
        print("Name : " + self.name)
        print("Age : " + str(self.age))
        print("Place : " + self.place)

    @classmethod
    def add_year(cls):
        cls.year = cls.year + 1

    @staticmethod
    def display_welcome():
        print("welcome")

CrossroadsTeamMember.display_welcome()

x = CrossroadsTeamMember("amal", 45, "calicut")
y = CrossroadsTeamMember("anil", 17, "kottayam")

x.display()
y.display()

print("------------------------")

CrossroadsTeamMember.year = CrossroadsTeamMember.year + 1
x.add_age()
y.add_age()

x.display()
y.display()

print("------------------------")
CrossroadsTeamMember.add_year()

x.add_age()
y.add_age()
x.relocate("delhi")
y.relocate("mumbai")

x.display()
y.display()
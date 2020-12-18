class MySampleClass:
    def hello(self, n):
        self.name = n
    def print_name(self):
        print(self.name)


x = MySampleClass()
y = MySampleClass()
name = "jinvy thomans"
x.hello(name)
y.hello("sithara menon")

x.print_name()
y.print_name()
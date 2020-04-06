import random

class Greeter(object):
    def hello(self):
        print("Hello")

    def goodbye(self):
        print("Good Bye")

g=Greeter()
g.hello()
g.goodbye()

class Die(object):
    def __init__(self,sides):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)


d = Die(6)
print(d.roll())
print(d.roll())
print(d.roll())



d = Die(10)
print(d.roll())
print(d.roll())
print(d.roll())

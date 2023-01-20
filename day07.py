class Fruit:
    color = 'red'

blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)

blueberry.color ='blue'
print(blueberry.color)
print(Fruit.color)

Fruit.color = 'orange'
print(Fruit.color)
print(blueberry.color)

new_fruit = Fruit()
print(new_fruit.color)

class A():
    count = 0
    def __init__(self):
        A.count = A.count + 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

easy_a=A()
print(A.kids())


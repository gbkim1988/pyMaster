# Factory/shapefact1/NestedShapeFactory.py
import random

class Shape(object):
    types = []

# 함수로 팩토리를 구성한 것에 특이함을 느껴라. 하지만, 파이썬은 모두 객체이다.
def factory(type):
    class Circle(Shape):
        def draw(self): print("Circle.draw")
        def erase(self): print("Circle.erase")

    class Square(Shape):
        def draw(self): print("Square.draw")
        def erase(self): print("Square.erase")

    if type == "Circle": return Circle()
    if type == "Square": return Square()
    assert 0, "Bad shape creation: " + type

def shapeNameGen(n):
    for i in range(n):
        yield factory(random.choice(["Circle", "Square"]))

# Circle() # Not defined

for shape in shapeNameGen(7):
    shape.draw()
    shape.erase()

# try to create Circle directly
factory.Circle().draw()
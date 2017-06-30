# Factory/shapefact1/ShapeFactory1.py
# A simple static factory method.
from __future__ import generators
import random

class Shape(object):
    # Create based on class name:
    def factory(type):
        #return eval(type + "()")
        if type == "Circle": return Circle()
        if type == "Square": return Square()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")

# Generate shape name strings:
def shapeNameGen(n):
    # 이 부분을 짚고 넘어갈 필요가 있다.
    # __subclasses__ 메서드는 Shape 객체의 타입을 출력한다.
    # 아래의 코드가 실행되면, 아래와 같은 클래스들의 목록을 확보할 수 있다.

    # [<class '__main__.Circle'>, <class '__main__.Square'>]
    types = Shape.__subclasses__()
    print(types)
    # 이렇게도 생성할 수 있는데, 그렇게 하지 않는 이유는? 
    print(types[0]().draw())
    for i in range(n):
        yield random.choice(types).__name__

shapes = \
  [ Shape.factory(i) for i in shapeNameGen(7)]

for shape in shapes:
    shape.draw()
    shape.erase()
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def square(self):
        return self.w * self.h

    def perimeter(self):
        return self.w * 2 + self.h *2



Obj1 = Rectangle(150, 450)
print(Obj1.square())
print(Obj1.perimeter())

Obj2 = Rectangle(200, 500)
print(Obj2.square())
print(Obj2.perimeter())

Obj3 = Rectangle(7, 35)
print(Obj3.square())
print(Obj3.perimeter())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


result = Math(5, 3)
print(result.addition())
print(result.multiplication())
print(result.division())
print(result.subtraction())



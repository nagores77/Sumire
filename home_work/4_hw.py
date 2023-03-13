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


class Button:
    def __init__(self, text, elem, loc=None):
        self.text = text
        self.elem = elem
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)


text_box = Button('Text Box', 'Кнопка')
check_box = Button('Check Box', 'Кнопка')
radio_button = Button('Radio Button', 'Кнопка')
web_table = Button('Web Table', 'Кнопка')
buttons = Button('Buttons', 'Кнопка')
links = Button('Links', 'Кнопка')
broken_links = Button('Broken Links', 'Кнопка')
upload_download = Button('Upload and Download', 'Кнопка')
dynamic_properties = Button('Dynamic Properties', 'Кнопка')

print(text_box.text)
print(text_box.click())

print(check_box.text)
print(check_box.click())

print(radio_button.text)
print(radio_button.click())

print(web_table.text)
print(web_table.click())

print(buttons.text)
print(buttons.click())

print(links.text)
print(links.click())

print(broken_links.text)
print(broken_links.click())

print(upload_download.text)
print(upload_download.click())

print(dynamic_properties.text)
print(dynamic_properties.click)








from task_9_checks import Checks
class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


search = Input('#Поиск', '/poisk')


number = Input('Twenty', '/twenty')
print(number.text, search.loc)

class Button (Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


back = Button('Назад', '/back')
up = Button('Вверх', '/up')

print(back.text, up.loc)

class Title(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


main = Title('Site', 'main_link')
subtitle = Title('About', '/link')

print(main.text, subtitle.loc)

class Link(Checks):
    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


home_page = Link('Home', '/home_page')
sub_page = Link('Sub_page', '/sub_page')

print(home_page.text, sub_page.loc)

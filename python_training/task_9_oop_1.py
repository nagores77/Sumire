class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Input('#Поиск', '/poisk')


number = Input('Twenty', '/twenty')
print(number.text, search.loc)

class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


back = Button('Назад', '/back')
up = Button('Вверх', '/up')

print(back.text, up.loc)

class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


main = Title('Site', 'main_link')
subtitle = Title('About', '/link')

print(main.text, subtitle.loc)

class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


home_page = Link('Home', '/home_page')
sub_page = Link('Sub_page', '/sub_page')

print(home_page.text, sub_page.loc)

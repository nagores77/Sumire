a: int = 5
b: str = 'строка'
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent('123', 123))


def indent_1(s: str = '') -> int:
    return len(s)

print(indent_1())


def add_2(x:list, y: list) -> int:
    return(max(len(x), len(y)))

print(add_2([1,2], [3,4,5]))


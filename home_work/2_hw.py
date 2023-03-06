def task_1(a:int=1, b:float=17.07, c:str='Алтай', d:list=[1,7,14], e:bool=True) ->tuple:
    return (type(a), type(b), type(c), type(d), type(e))


print(task_1())

def task_2(a = [1, 2, 3, 5, 8, 13, 21]) ->int:
    return a[0:3]
print(task_2(), '- последовательность Фибоначчи')

def task_3(l: int)->int:
    return l ** 2

print(task_3(7))



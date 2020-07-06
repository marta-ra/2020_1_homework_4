'''
Декоратор типов
Напишите декоратор, который проверял бы тип параметров функции следующим образом: При вызове без аргументов осуществлял бы
конвертацию параметров и возвращаемого значения в указанные типы:

@typed
def add(a: int, b: int) -> str:
    return a + b

add("3", 5) -> "8"
add(2.35, True) -> "3"
При вызове с параметром strict=True выбрасывал бы исключение при неправильной передаче параметров:

@typed(strict=True)
def convert_upper(msg: str) -> str:
    return msg.upper()

convert_upper('abc') -> 'ABC'
convert_upper(5) -> TypeError('`convert_upper` argument `msg` required to be a `str` instance')
Если типы параметров функции не указаны декоратор должен предполагать их тип как Any:

@typed
def acc(a, b, c):
    return a + b + c

acc('a', 'b', 'c') -> 'abc'
acc(5, 6, 7) -> 18
acc(0.1, 0.2, 0.4) -> 0.7000000000000001
'''


class MyClass:

    def typed1(f):
        def wrapper(self, *args):
            lst = []
            for arg in args:
                arg = int(arg)
                lst.append(arg)
            result = str(f(self, *lst))
            return result
        return wrapper


    def typed2(strict=False):
        def outer(f, *args):
            def wrapper(self, *args):
                if strict==True:
                    if type(*args) == str:
                        result = f(self, *args)
                    else:
                        raise TypeError('`convert_upper` argument `msg` required to be a `str` instance')
                return result
            return wrapper
        return outer

    def typed3(f):
        def wrapper(self, *args):
            result = f(self, *args)
            return result
        return wrapper


    @typed1
    def add(self, a: int, b: int) -> str:
        return a + b


    @typed2(strict=True)
    def convert_upper(self, msg: str) -> str:
        return msg.upper()


    @typed3
    def acc(self, a, b, c):
        return a + b + c


if __name__ == '__main__':
    # Here we can make console input and check how function works

    a = 4
    b = True

    result = MyClass().add(a, b)

    print(result)

    msg = '6'
    result = MyClass().convert_upper(msg)
    print(result)
    #
    a = 'a'
    b = 'b'
    c = 'c'
    # a = 5
    # b = 5
    # c = 1
    # a = 0.1
    # b = 0.2
    # c = 0.4
    result = MyClass().acc(a, b, c)
    print(result)

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

    def typed(f):
        def wrapper(self, *args, **kwargs):
            lst = []
            for arg in args:
                arg = int(arg)
                lst.append(arg)
            result = str(f(self, *lst, **kwargs))
            return result

        return wrapper

    @typed
    def add(self, a: int, b: int) -> str:
        return a + b
#____________________________________

    def typed2(**kwargs):
        def outer(f):
            def wrapper(self, a):
                # не совсем то что нужно, но как смогла
                if type(a) != str:
                    result = TypeError('`convert_upper` argument `msg` required to be a `str` instance')
                else:
                    result = f(self, a)
                return result
            return wrapper
        return outer

    @typed2(strict=True)
    def convert_upper(self, msg: str) -> str:
        return msg.upper()


    # @typed
    # def acc(self, a, b, c):
    #     return a + b + c


if __name__ == '__main__':
    # Here we can make console input and check how function works

    a = 5
    b = True

    result = MyClass().add(a, b)

    print(result)

    msg = ['h']
    result = MyClass().convert_upper(msg)
    print(result)
    #
    # a = '5'
    # b = '6'
    # c = '2'
    # result = MyClass().acc(a, b, c)
    # print(result)

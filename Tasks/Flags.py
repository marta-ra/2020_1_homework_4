'''
Флаги
Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n флагов. Изображение одного флага имеет размер 4×4 символов, между двумя соседними флагами также имеется пустой (из пробелов)
столбец. Разрешается вывести пустой столбец после последнего флага. Внутри каждого флага должен быть записан его номер — число от 1 до n.

Пример
1.

3

+___ +___ +___
|1 / |2 / |3 /
|__\ |__\ |__\
|    |    |
2.

2

+___ +___
|1 / |2 /
|__\ |__\
|    |

'''


class MyClass:


    def _decor(func):
        def wrapper(self, *args, **kwargs ):
            for i in args:
                if int(i) > 0 and int(i) < 10:
                    level1 = str('+___ ' * int(*args))
                    level3 = str('|__\ ' * int(*args))
                    level4 = str('|    ' * int(*args))
                    print(level1)
                    print(func(self, *args, **kwargs))
                    print(level3)
                    print(level4)
                    seccess = func(self, *args, **kwargs)
                    return seccess
                else:
                    print('Enter value greater than 0 and less than 10')
                    error = 'Enter value greater than 0 and less than 10'
                    return error
        return wrapper



    @_decor
    def flags(self, expression):

        level2 = ''
        for i in self.lst(expression):
            num = str(self.lst(expression)[i-1])
            level2 += '|' + num + ' / '

        return level2

    def lst(self, expression):
        lst = []
        for a in range(1, int(expression) + 1):
            lst.append(a)
            a += 1
        return lst


if __name__ == '__main__':
#     # Here we can make console input and check how function works
#
    var = input('Input Number of Flags: ')

    result = MyClass().flags(var)



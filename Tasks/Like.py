'''
Мне нравится 👍
Создайте функцию, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).

def likes(*arr: str) -> str:
    pass
Примеры:

likes() -> "no one likes this"
likes("Peter") -> "Peter likes this"
likes("Jacob", "Alex") -> "Jacob and Alex like this"
likes("Max", "John", "Mark") -> "Max, John and Mark like this"
likes("Alex", "Jacob", "Mark", "Max") -> "Alex, Jacob and 2 others like this"
Бонусные очки
Функция работает на нескольких языках и кодировках - язык ответа определяется по языку входного массива.
'''


class MyClass:

    def likes(self, var):
        if var != '':
            new_input = self.create_lst(var)
            condition = len(self.create_lst(var))
            result = 0

            if condition == 1:
                result = new_input[0] + ' likes this'
            elif condition == 2:
                result = new_input[0] + ' and ' + new_input[1] + ' like this'
            elif condition == 3:
                result = new_input[0] + ', ' + new_input[1] + ' and ' + new_input[2] + ' like this'
            elif condition > 3:
                others = str(condition - 2)
                result = new_input[0] + ', ' + new_input[1] + ' and ' + others + ' others like this'


        else:
            result = "no one likes this"
        return result

    def del_char(self, var):
        symb = '",'
        for char in symb:
            var = var.replace(char, "")
        return var

    def create_lst(self, var):
        a = self.del_char(var)
        list_of_names = list(a.split(' '))
        return list_of_names

if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input names: ')

    result = MyClass().likes(var)

    print(result)

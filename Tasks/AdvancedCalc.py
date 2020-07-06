'''
Инженерный калькулятор
Напишите программу - инженерный калькулятор. После запуска программа открывает интерактивную оболочку, в которую можно
 вводить комманды:

user@machine:~$ python calc.py
Advanced calculator. Author: [Student Name], Version: 1.0.0
~ ...
Базовые требования
Программа воспринимает введённые пользователем математические выражения и правильно их интепретирует:
~ 5 + 4
9
~ 10 - 3 + 1
8
~ 2 ** 3 - 1
7
Программа знает о приоритете операторов
~ 2 + 3 * 4
14
~ 8 / 2 * 3
12
Программа поддерживает изменение приоритета при помощи скобок
~ 3 * (2 + 1)
9
~ 5 + (2 - 2 * (3 + 7))
-13
Использование eval, exec, compile запрещено.
Дополнительные баллы (каждый подпункт - 1 балл)
Программа воспринимает основные математические функции и константы:
~ sqrt(3) + ln(e) - pi
-0.4095418460209159
Программа поддерживает переменные
~ x = 5
~ x
5
~ x + 3
8
Программа поддерживает оператор ' для взятия производной простейших функций
~ x = 2
~ (x ** 3)'
12
~ sin(2 * x)'
-0.8322936730942848
Программа поддерживает объявление функций
~ f(x) = x ** 2 + tg(x)'
~ f(5)
37.427881707458354

'''


class MyClass:
    def __init__(self, string, vars={}):
        self.string = string
        self.index = 0
        self.vars = {
            'pi': 3.141592653589793,
            'e': 2.718281828459045
        }
        for var in vars.keys():
            if self.vars.get(var) != None:
                raise Exception('Cannot redefine the value of ' + var)
            self.vars[var] = vars[var]

    def getValue(self):
        value = self.parseExpression()
        self.skipWhitespace()
        if self.hasNext():
            raise Exception(
                'Unexpected character found: ' +
                self.peek() + ' at index ' + str(self.index))
        return value

    def peek(self):
        return self.string[self.index:self.index + 1]

    def hasNext(self):
        return self.index < len(self.string)

    def skipWhitespace(self):
        while self.hasNext():
            if self.peek() in ' \t\n\r':
                self.index += 1
            else:
                return

    def parseExpression(self):
        return self.parseAddition()

    def parseAddition(self):
        values = [self.parseMultiplication()]
        while True:
            self.skipWhitespace()
            char = self.peek()
            if char == '+':
                self.index += 1
                values.append(self.parseMultiplication())
            elif char == '-':
                self.index += 1
                values.append(-1 * self.parseMultiplication())
            else:
                break
        return sum(values)

    def parseMultiplication(self):
        values = [self.parseParenthesis()]
        while True:
            self.skipWhitespace()
            char = self.peek()
            if char == '*':
                self.index += 1
                values.append(self.parseParenthesis())
            elif char == '/':
                div_index = self.index
                self.index += 1
                denominator = self.parseParenthesis()
                if denominator == 0:
                    raise Exception('Division by 0 kills baby whales (occured at index ' +
                        str(div_index) + ')')
                values.append(1.0 / denominator)
            else:
                break
        value = 1.0
        for factor in values:
            value *= factor
        return value

    def parseParenthesis(self):
        self.skipWhitespace()
        char = self.peek()
        if char == '(':
            self.index += 1
            value = self.parseExpression()
            self.skipWhitespace()
            if self.peek() != ')':
                raise Exception('No closing parenthesis found at character '
                    + str(self.index))
            self.index += 1
            return value
        else:
            return self.parseNegative()

    def parseNegative(self):
        self.skipWhitespace()
        char = self.peek()
        if char == '-':
            self.index += 1
            return -1 * self.parseParenthesis()
        else:
            return self.parseValue()

    def parseValue(self):
        self.skipWhitespace()
        char = self.peek()
        if char in '0123456789.':
            return self.parseNumber()
        else:
            return self.parseVariable()

    def parseVariable(self):
        self.skipWhitespace()
        var = ''
        while self.hasNext():
            char = self.peek()
            if char.lower() in '_abcdefghijklmnopqrstuvwxyz0123456789':
                var += char
                self.index += 1
            else:
                break

        value = self.vars.get(var, None)
        if value == None:
            raise Exception('Unrecognized variable: ' + str(var))
        return float(value)

    def parseNumber(self):
        self.skipWhitespace()
        strValue = ''
        decimal_found = False
        char = ''

        while self.hasNext():
            char = self.peek()
            if char == '.':
                if decimal_found:
                    raise Exception('Found an extra period in a number at character ' + str(self.index) +'. Are you European?')
                decimal_found = True
                strValue += '.'
            elif char in '0123456789':
                strValue += char
            else:
                break
            self.index += 1

        if len(strValue) == 0:
            if char == '':
                raise Exception('Unexpected end found')
            else:
                raise Exception('I was expecting to find a number at character ' +
                    str(self.index) + ' but instead I found a ' + char + '. Whats up with that?')

        return float(strValue)


def evaluate(expression, vars={}):
    try:
        p = MyClass(expression, vars)
        value = p.getValue()
    # except Exception as ex:
    #     msg = ex.message
    #     raise Exception(msg)
    except AttributeError:
        raise ('I can not recognize the entered expression')

    # Возвращает целочисленный тип, если ответ является целым числом
    if int(value) == value:
        return int(value)


    epsilon = 0.0000000001
    if int(value + epsilon) != int(value):
        return int(value + epsilon)
    elif int(value - epsilon) != int(value):
        return int(value)

    return value


if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input()

    result = evaluate(var)

    print(result)



'''
Из молекулы в атомы
Напишите функцию, которая, принимая как параметр строку - формулу молекулы, возвращала бы атомы из этой молекулы и их количество в виде Dict[str, int]:

def parse_molecule(molecule: str) -> dict:
    pass
Примеры:¶
H2O -> {H: 2, O: 1}
Mg(OH)2 -> {Mg: 1, O: 2, H: 2}
K4[ON(SO3)2]2 -> {K: 4, O: 14, N: 2, S: 4}
Замечания:
Скобки в формулах могут быть круглыми, квадратными и фигурными. Такжи они могут быть вложены друг в друга.
Индекс после скобки означает количество раз, которое повторяется каждый атом внутри скобок.
Индекс после скобки необязателен. Если его нет, значит содержимое скобок повторяется 1 раз.
'''


import re
from collections import Counter

class MyClass:
    global ATOM_REGEX
    global OPENERS
    global CLOSERS
    ATOM_REGEX = '([A-Z][a-z]*)(\d*)'
    OPENERS = '({['
    CLOSERS = ')}]'

    def typed(f):
        def wrapper(self, *args):
            result = f(self, *args)
            if result == {}:
                result = 'Enter the formula of the molecule'
            else:
                result = f(self, *args)
            return result
        return wrapper

    def is_balanced(self, formula):
        # проверка ввода, все ли скобки поставлены попарно
        c = Counter(formula)
        return c['['] == c[']'] and c['{'] == c['}'] and c['('] == c[')']

    def _dictify(self, tuples):
        #  преобразование кортежа в словарь автомов
        res = dict()
        for atom, n in tuples:
            try:
                res[atom] += int(n or 1)
            except KeyError:
                res[atom] = int(n or 1)
        return res

    def _fuse(self, mol1, mol2, w=1):
        # составляется соловарь молекул
        return {atom: (mol1.get(atom, 0) + mol2.get(atom, 0)) * w for atom in set(mol1) | set(mol2)}

    def _parse(self, formula):
        q = []
        mol = {}
        i = 0

        while i < len(formula):
            token = formula[i]

            if token in CLOSERS:
                m = re.match('\d+', formula[i + 1:])
                if m:
                    weight = int(m.group(0))
                    i += len(m.group(0))
                else:
                    weight = 1

                submol = self._dictify(re.findall(ATOM_REGEX, ''.join(q)))
                return self._fuse(mol, submol, weight), i

            elif token in OPENERS:
                submol, l = self._parse(formula[i + 1:])
                mol = self._fuse(mol, submol)
                # пропустить уже прочитанный submol
                i += l + 1
            else:
                q.append(token)

            i += 1

        return self._fuse(mol, self._dictify(re.findall(ATOM_REGEX, ''.join(q)))), i
    @typed
    def parse(self, formula):
        # разбор введенной формула (парсинг) и возврат словаря с количеством каждого атома
        if not self.is_balanced(formula):
            raise ValueError("Watch your brackets ![{]$[&?)]}!]")

        return self._parse(formula)[0]



if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input formula: ')

    result = MyClass().parse(var)

    print(result)

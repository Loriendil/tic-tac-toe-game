# Игра крестики-нолики
# правила взяты из статьи на Хабре.
"""
Обновление и улучшение кода
Читаемость:
Ч1. Более говорящие имена переменных (например, elem и e_type можно переименовать в row и player_type
Ч2. docstrings это  """ """. Использование print(add.__doc__) или help(add), где
add() это функция с docstring

Оптимизация:
О1. Вложенные циклы для проверки условий победы можно оптимизировать.
О2. Вместо проверки каждого элемента доски для каждого типа игрока,
более эффективную проверку можно организовать для снижения количества проверок.

Масштабируемость:
М1. Если будет развитие игры, то функциональный подход будет ограничением проекта.

Безопасность:
Б1. Размер игрового поля подразумевается положительным числом, но пользователя никто не проверяет.
"""

# Интерпретатор в браузере: https://www.programiz.com/python-programming/online-compiler/

import PvEvP

def greetings(phrase):
    print(phrase)
    ans = input()
    if ans.upper() == 'Q':
        return -3
    else:
        if ans.upper() == 'F':
            PvEvP.play(2)
            return 3
        elif ans.upper() == 'C':
            PvEvP.play(-2)
            return 3
        else:
            return -3

print('Hello! It is a tic-tac-toe game')
print('Rules are:')
print('1. An empty board of n x n cells.')
print('2. Two players take turns placing their piece in an empty cell')
print("3. Any horizontal, vertical or diagonal row filled with a player's piece brings him a win and ends the game")
print('4. When there are no more empty cells, the game also ends, in a draw.')
print("5. For simplicity of display, we choose capital X and O as the player's pieces")
print('and a space for an empty cell')
print('6. Let the player for X go first.')

count = 0
first_time = 'Do you want to play with your friend [F] or your computer [C]? (for exit press "Q")'
second_time = 'Do you want to play again with your friend [F] or your computer [C]? (for exit press "Q")'
while count >= 0:
    if count == 0:
        count = greetings(first_time)
    if count > 0:
        count = greetings(second_time)
print('Have a nice day, sir!')
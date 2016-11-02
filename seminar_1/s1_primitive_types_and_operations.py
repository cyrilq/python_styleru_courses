# Однострочные комментарии начинаюся со знака #.

""" Многострочные комменты можно писать
    через три кавычки,
    двойные или одинарные
"""

################################
## 1. Базовые типы и операции ##
################################

# Числа
3  # => 3

# Математика работает стандартно
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20

# Кроме деления, которое возвращает по умолчанию float
35 / 5  # => 7.0

# Целочисленное деление всегда округляется вниз, для положительных и отрицательных чисел
5 // 3       # => 1
5.0 // 3.0   # => 1.0 
-5 // 3      # => -2
-5.0 // 3.0  # => -2.0

# Если в выражении есть float, возвращается тоже float
3 * 2.0  # => 6.0

# Операция остатка
7 % 3  # => 1

# Возведение в степень
2**4  # => 16

# Скобки работают как обычно
(1 + 3) * 2  # => 8

# Булевые переменные (регистр!)
True
False

# Для отрицания используем not
not True   # => False
not False  # => True

# Булевы операции
# "and" и "or" пишем в нижнем регистре
True and False  # => False
False or True   # => True

# Смотрите, как булевы переменные ведут себя с целочисленными:
0 and 2     # => 0
-5 or 0     # => -5
0 == False  # => True
2 == True   # => False
1 == True   # => True

# Равенство обозначается ==
1 == 1  # => True
2 == 1  # => False

# Неравенство это !=
1 != 1  # => False
2 != 1  # => True

# Сравнения больше/меньше
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Можно составлять из них цепочки (привет, си шарп!)
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is проверяет, ссылаются ли переменные на один объект, а == проверяет
# указывают ли объекты на одно значение (value)
a = [1, 2, 3, 4]  # а указывает на новый лист, [1, 2, 3, 4]
b = a             # b ссылается на тот же лист
b is a            # => True
b == a            # => True, их значения одинаковы
b = [1, 2, 3, 4]  # b теперь указывает на новый лист, [1, 2, 3, 4]
b is a            # => False
b == a            # => True, их значения по-прежнему равны

# Строки можно складывать
"Hello " + "world!"  # => "Hello world!"

# К строке можно обращаться как к массиву символов
"This is a string"[0]  # => 'T'

# Так находим длину строки
len("This is a string")  # => 16

# .format используем для форматирования
"{} is learning {}".format("Malika", "Python")  
# => "Malika is learning Python"

# You can repeat the formatting arguments to save some typing.
"{0} loves {1}, and {2} loves {1}".format("Theodore", "pasta", "Cyril")
# => "Theodore loves pasta, and Cyril loves pasta"

# Если лень считать, можно юзать ключевые слова.
"{name} wants to drink {food}".format(name="Cyril", food="whisky")  # => "Cyril wants to drink whisky"

# None, 0, и пустые строки/листы/словари эквивалентны False.
# Все остальные — True
bool(0)   # => False
bool("")  # => False
bool([])  # => False
bool({})  # => False
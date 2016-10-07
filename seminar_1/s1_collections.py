##################
## 2. Коллекции ##
##################

# По умолчанию конец стоки — переход на новую ('\n').
# Можно изменить его по желанию.
print("Hello, World", end="!")  # => Hello, World!

# Так можно получить стоку из консоли
input_string_var = input("Enter some data: ") # Получаем из консоли строку

# Условные операторы можно использовать в одну строку:
"Привет!" if 3 > 2 else "Пока!"  # => "Привет!"

# Лист хранит значения
li = []
# Можно заполнить его сразу 
other_li = [4, 5, 6]

# Добавляем элементы при помощи append
li.append(1)    # li is now [1]
li.append(2)    # li is now [1, 2]
li.append(3)    # li is now [1, 2, 3]
li.append(4)    # li is now [1, 2, 3, 4]
# Убираем последний элемент при помощи pop
li.pop()        # => 4 and li is now [1, 2, 3]

# К листу можно обращаться как к обычному массиву
li[0]   # => 1
# Доступ к последнему элементу
li[-1]  # => 3

# За границы выходить нельзя:
li[4]  # Raises an IndexError

# Можно получать доступ к опр. части листа через срезы (слайсы)
li[1:3]   # => [2, 3]
li[2:]    # => [3, 4]
li[:3]    # => [1, 2, 3]
# С шагом 2
li[::2]   # =>[1, 4]
# Реверсим лист
li[::-1]  # => [3, 4, 2, 1]
# Все работает по шаблону
# li[start:end:step]

# Опр. элемент можно удалить при помощи del
del li[2]  # li is now [1, 2, 4]

# remove убирает первый встреченный элемент:
li.remove(2)  # li is now [1, 4]
li.remove(2)  # ValueError, потому что 2 нет в листе

# Можно вставить опр. элемент в опр. место в листе
li.insert(1, 2)  # Снова [1, 2, 4] 

# Можно получить индекс опр. элемента
li.index(2)  # => 1
li.index(3)  # ValueError, потому что 3 нет в листе

# Листы можно складывать, при таком сложении сами листы-слагаемые не меняются!
li + other_li  # => [1, 2, 3, 4, 5, 6]

# А так меняются
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]

# Можно проверить наличие элемента в листе при помощи in
1 in li  # => True

# Тьюпл (или кортеж) — это неизменяемый лист
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True
# Тьюплы можно использовать даже без скобок 
a, b, c = (1, 2, 3)  
a, *b, c = (1, 2, 3, 4)  
d, e, f = 4, 5, 6
e, d = d, e 


# Словари ведут себя обычно
empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}

# Ключи словарей обязаны принадлежать неизменяемому типу! 
invalid_dict = {[1,2,3]: "123"}  # => TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Values могут быть любого типа

# Искать значения можно квадратными скобками
filled_dict["one"]  # => 1

# Проверяем наличие ключа при помощи "in"
"one" in filled_dict  # => True
1 in filled_dict      # => False
filled_dict["four"]  # KeyError

# Используем метод "get()" во избежание ошибки 
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# Можно установить аргумент по умолчанию
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# Добавление в словарь
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
#filled_dict["four"] = 4        #another way to add to dict

# Удаление ключа
del filled_dict["one"]  # Removes the key "one" from filled dict

# Сеты (множества) — из названия понятно, что это (привет, дискра!)
empty_set = set()
some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}
invalid_set = {[1], 1}  # => TypeError: unhashable type: 'list'
valid_set = {(1,), 1}
filled_set.add(5) 
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}
{1, 2} >= {1, 2, 3} # => False
{1, 2} <= {1, 2, 3} # => True
2 in filled_set   # => True
10 in filled_set  # => False

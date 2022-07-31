"""Задача_7 25 баллов
Тема frozenset.
создать frozenset (Прочитать что это где вам удобно)
необходимо посчитать длинну этой коллекции без помощи функции len().
И вывести ее в косноль."""
# create a frozenset
animals: frozenset = frozenset(["pig", "pig", "bear", "cat", "cat"])
# create a set step variable
set_length: int = 0
# create an interpretable variable from our frozenset
for i in animals:
    # with each new value of the interpreted variable, we add one to our step variable
    set_length += 1
# output the result of the number of non-repeatable objects
print(set_length)

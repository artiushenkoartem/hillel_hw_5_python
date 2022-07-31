"""Задача_4 25 баллов
написать программу которая будет создавать список методов из доступных методов питон объектов.
Под доступными подразумевается методы без подчеркиваний. Фунции dir() т.е для объекта set должен быть
список методов ['add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'isdisjoint',
'issubset', 'issuperset', 'pop', 'remove', 'union', 'update']"""
# create a variable with a full list of methods
set_methods: list = (dir(set))
# create an empty list
new_set_methods: list = []
# create an interpretable variable from the list of methods
for i in set_methods:
    # set the condition for the interpreted variable
    if '_' not in i:
        # if the condition for the interpreted variable is met, then we transfer it to an empty list
        new_set_methods.append(i)
# output the resulting list of methods
print(new_set_methods)

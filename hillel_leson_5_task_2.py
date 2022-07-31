"""Задача_2. 5 баллов
Дан список с повторяющимися значениями необходимо из него удалить все определенные
значения используя while цикл.
Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg
Результат: ['bear', 'milk']"""
# create our variable
grocery_list: list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
# show it to the user
print(grocery_list)
# we ask the user which element from the variable he wants to remove
value_to_remove: str = input('Fill up value for delete:')
# make the element mismatch condition
if value_to_remove not in grocery_list:
    # if the element is not in our variable, then we ask the user again
    value_to_remove = input('Fill up value for delete again:')
# if the element is in our variable, then we enter the loop body
while True:
    # if the element is in our variable,remove element from variable
    if value_to_remove in grocery_list:
        grocery_list.remove(value_to_remove)
    # if now there is no element to delete in the variable, then we display the formatted variable to the user
    else:
        print(f" {grocery_list = }\n")
        break

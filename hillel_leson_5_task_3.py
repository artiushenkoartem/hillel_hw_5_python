"""Задача_3. 10 баллов
Тема while and else
дан список произвольный с int нужно вывести "all numbers are even" если все четные и NO если нет
Пример входных данных: [11, 23, 65, 44, 76, 533]
Результат: NO
Пример входных данных: [12, 22, 66, 44, 76, 534]
Результат: all numbers are even"""
# create your list of numbers
user_list: list = [12, 22, 66, 44, 76, 534]
# create a variable representing our position in the list
list_step: int = 0
# we create an interpreted variable that will run through our list
for i in user_list:
    # create a condition for odd numbers
    if i % 2 != 0:
        # if the condition is met for all elements of the variable, then display the text
        print("NO")
        break
    # if the condition is not met, then we add one to our variable position in the list
    else:
        list_step += 1
# create a condition for the end of the list
if list_step == len(user_list):
    # if the first condition is not met and the second is met, then we display the text
    print("All numbers are even")

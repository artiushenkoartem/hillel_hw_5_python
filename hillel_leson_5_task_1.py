"""Задача 1. 10 баллов
пользователь вводит пароль первый раз система запоминает и просит повторить пароль проверяет
его если нет то просит повторить. А если совпал то сообщение."""
# create variable from user input
user_password: str = input("Fill up you password:")
# create a cycle
while True:
    # set the condition for the correspondence of two user variables
    if user_password == input("Fill up you password again:"):
        # if the condition is met, display the text
        print("welcome dear user\n")
        break
    # if the condition is not met, return to the beginning of the loop
    else:
        continue

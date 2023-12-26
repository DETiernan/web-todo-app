# This program creates a todolist in a file
import time

def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is now", now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, remove or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # add list item to a file
        todo = user_action[4:]
        todos = get_todos('files/todos.txt')
        todos.append(todo + '\n')
        with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

    elif user_action.startswith("show"):
        # get list from a file
        todos = get_todos('files/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        todos = get_todos('files/todos.txt')
        # change a list item in a file
        number = int(input("Number of todo to edit: "))
        number = number -1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo

        file = open('files/todos.txt', 'w')
        file.writelines(todos)
        file.close()

    elif user_action.startswith("remove"):
        todos = get_todos('files/todos.txt')

        number = int(input("Number of the todo to remove: "))
        todos.pop(number - 1)

        file = open('files/todos.txt', 'w')
        file.writelines(todos)
        file.close()

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("Bye!")
# This program creates a todolist in a file
from functions import get_todos, write_todos
import time
# import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is now", now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # add list item to a file
        todo = user_action[4:]
        todos = get_todos(filepath="files/todos.txt")
        todos.append(todo + '\n')
        write_todos(todos, "files/todos.txt")

    elif user_action.startswith("show"):
        # get list from a file
        todos = get_todos('files/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        # change a list item in a file
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos('files/todos.txt')
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos, "files/todos.txt")
        except ValueError:
            print("Your command is invalid")
            continue
        except IndexError:
            print("Your command is invalid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos('files/todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            message = f"Todo {todo_to_remove.capitalize()} was removed from the list."
            print(message)
            write_todos(todos, "files/todos.txt")
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("You forgot to enter a number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("Bye!")

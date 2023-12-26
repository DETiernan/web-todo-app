import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label, input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    # print(values['todo'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todo = values['todos']
        case sg.WINDOW_CLOSED:
            break

window.close()
import PySimpleGUI as sg


def main():
    file = open("passwords.txt", "r")

    passwords = file.readlines()

    passwords_untouched = passwords[:]

    for i in range(len(passwords)):
        passwords[i] = f"{i+1}.    " + passwords[i]

    layout = [
        [sg.Listbox(values = passwords, size=(130, 5))],
        [sg.Button("Въведи")]
    ]

    window = sg.Window('To Do List Example', layout, font="Helvetica 12", size=(550,150))
    event, values = window.read()

    if event == "Въведи":
        window.close()
        return passwords_untouched[int(values[0][0][0]) - 1].rsplit(' ', 1)[0], passwords_untouched[int(values[0][0][0]) - 1].rsplit(' ', 1)[1]



import PySimpleGUI as sg

def main():
    layout = [
        [sg.Text('Въведете трите си имена ')],
        [sg.Input()],
        [sg.Text('Въведете вашето ЕГН ')],
        [sg.Input()],
    ]
    first_window = sg.Window('Начален прозорец', layout, font="Helvetica 12")

    Name, SSN = first_window.read()



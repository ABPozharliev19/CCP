import PySimpleGUI as sg
import tokens


def main():
    layout = [
        [sg.Text('Въведете трите си имена ')],
        [sg.Input()],
        [sg.Text('Въведете ЕГН-то си ')],
        [sg.Input()],
    ]
    first_window = sg.Window('Начален прозорец', layout)

    first_window.read()

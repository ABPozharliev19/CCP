import PySimpleGUI as sg
import tokens


def main():
    layout = [
        [sg.Text('Въведете трите си имена ')],
        [sg.Input()],
        [sg.Text('Въведете вашето ЕГН ')],
        [sg.Input()],
    ]
    first_window = sg.Window('Начален прозорец', layout, font="Helvetica 12")

    first_window.read()



main()

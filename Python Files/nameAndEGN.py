import PySimpleGUI as sg
import placeOfBirth as secondPage

def main():
    layout = [
        [sg.Text('Въведете трите си имена ', justification='center')],
        [sg.Input()],
        [sg.Text('Въведете вашето ЕГН ')],
        [sg.Input()],
        [sg.Button('Напред')]
    ]
    first_window = sg.Window('Начален прозорец', layout, font="Helvetica 12")

    temp, name_and_egn = first_window.read()
    print(name_and_egn)
    secondPage.main()


main()

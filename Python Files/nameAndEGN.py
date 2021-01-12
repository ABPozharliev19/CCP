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
    first_window = sg.Window('Начален прозорец', layout, font="Helvetica 12", icon="../Logo.ico")

    temp, name_and_egn = first_window.read()

    if temp != 'Напред':
        first_window.close()
        print(temp, name_and_egn)

    else:
        first_window.close()
        secondPage.main()


if __name__ == "__main__":
    main()


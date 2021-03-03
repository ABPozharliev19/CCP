import PySimpleGUI as sg
import place_of_birth as secondPage


name = ""
egn = ""


def main():
    layout = [
        [sg.Text('Въведете трите си имена ', justification='center')],
        [sg.Input()],
        [sg.Text('Въведете вашето ЕГН ')],
        [sg.Input()],
        [sg.Button('Напред')]
    ]
    first_window = sg.Window('Начален прозорец', layout, font="Helvetica 12", icon="../Logo.ico")

    event, name_and_egn = first_window.read()



    if event != 'Напред':
        first_window.close()

    else:
        first_window.close()
        secondPage.main()


if __name__ == "__main__":
    main()

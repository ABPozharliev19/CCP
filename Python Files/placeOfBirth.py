import PySimpleGUI as sg
import placeOfLife as thirdPage
import nameAndEGN as firstPage


def main():
    layout = [
        [sg.Text('Въведетe държавата на раждане')],
        [sg.Input()],
        [sg.Text('Въведете населеното място на раждане')],
        [sg.Input()],
        [sg.Button('Назад'), sg.Button('Напред')]
    ]
    second_window = sg.Window('Начален прозорец', layout, font = "Helvetica 12")

    temp, place_of_birth = second_window.read()

    if temp == 'Назад':
        second_window.close()
        firstPage.main()

    if temp is None:
        second_window.close()
        print(place_of_birth)

    else:
        second_window.close()
        thirdPage.main()

        # nice


if __name__ == "__main__":
    main()


import PySimpleGUI as sg
import place_of_life as thirdPage
import name_and_eng as firstPage


def main():
    ##### DECLARATION AND DESIGN OF THE PAGE LAYOUT ######
    layout = [
        [sg.Text('Въведетe държавата на раждане')],
        [sg.Input()],
        [sg.Text('Въведете населеното място на раждане')],
        [sg.Input()],
        [sg.Button('Назад'), sg.Button('Напред')]
    ]
    ######################################################

    # Define the window
    second_window = sg.Window('Начален прозорец', layout, font = "Helvetica 12", icon="../Logo.ico")

    # Makes the window show and stores every information in it in variables
    temp, place_of_birth = second_window.read()

    # If the button "Назад" is pressed
    if temp == 'Назад':
        second_window.close()
        firstPage.main()

    # If the application is closed by the "X" button
    if temp is None:
        second_window.close()
        print(place_of_birth)

    # The button "Напред" is pressed
    else:
        second_window.close()
        thirdPage.main()

        # nice


if __name__ == "__main__":
    main()


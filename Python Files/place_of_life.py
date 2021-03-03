import PySimpleGUI as sg
import applicant_quality as fourthPage
import place_of_birth as secondPage


def main():
    ####### WINDOW LAYOUT STARTS HERE #######
    layout = [
        [sg.Text('Държава', size=(45, 1), justification='center')],
        [sg.Input(size=(22, 1))],
        [sg.Text('Населено място', pad=(44, 0)), sg.Text('Пощенски код', pad=(46, 0))],
        [sg.Input(size=(21, 1)), sg.Input(size=(21, 1))],
        [sg.Text('Ж.к.')],
        [sg.Input()],
        [sg.Text('Бул / ул.')],
        [sg.Input()],
        [sg.Text('№', pad=(30, 1)), sg.Text('Бл.', pad=(30, 1)), sg.Text('Вх.', pad=(30, 1)),
         sg.Text('Ет.', pad=(30, 1)), sg.Text('Ап.', pad=(30, 1))],
        [sg.Input(size=(8, 1)), sg.Input(size=(8, 1)), sg.Input(size=(9, 1)), sg.Input(size=(8, 1)),
         sg.Input(size=(8, 1))],
        [sg.Button('Назад'), sg.Button('Напред')]
    ]

    #### WINDOW LAYOUT ENDS HERE ####

    # Define the window
    thirdWindow = sg.Window('Постоянен адрес', layout, font="Helvetica 12" , element_justification='center', icon="../Logo.ico")

    # Make the window show and read every information in it
    temp, place_of_life = thirdWindow.read()

    # If the window is closed by the "X" button
    if temp is None:
        thirdWindow.close()

    # If the button "Назад" is pressed
    elif temp == 'Назад':
        thirdWindow.close()
        secondPage.main()

    # The button "Напред" is pressed
    else:
        thirdWindow.close()
        fourthPage.main()


if __name__ == "__main__":
    main()

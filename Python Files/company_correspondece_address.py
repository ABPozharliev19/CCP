import PySimpleGUI as sg
import company_info as previous_page


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
    Window = sg.Window('Адрес за кореспонденция с НАП на територията на страната', layout, font="Helvetica 12" , element_justification='center', icon="../Logo.ico")

    # Make the window show and read every information in it
    events, place_of_life = Window.read()

    # If the window is closed by the "X" button
    if events is None:
        Window.close()

    # If the button "Назад" is pressed
    elif events == 'Назад':
        Window.close()
        previous_page.main()

    # The button "Напред" is pressed
    else:
        Window.close()
        # fourthPage.main()


if __name__ == "__main__":
    main()

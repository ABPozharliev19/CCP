import PySimpleGUI as sg
import place_of_life as thirdPage
import name_and_translated_name as nextWindow


def main():
    layout = [
        [sg.Text('Качество на заявителя', size=(45, 1), justification='center')],
        [sg.Radio('Търговец/лице, представляващо ЮЛНЦ', "RADIO1", default=True)],
        [sg.Radio('Адвокат с изрично пълномощно', "RADIO1")],
        [sg.Radio('Прокурист', "RADIO1")],
        [sg.Radio('Друго лице в предвидените по закон случаи', "RADIO1")],
        [sg.Button('Назад', pad=(100, 0)), sg.Button('Напред')]
    ]

    fourthWindow = sg.Window('Качество на заявителя ', layout, font="Helvetica 12", icon="../Logo.ico")

    temp, applicant_quality = fourthWindow.read()

    # If the window is closed by the "X" button
    if temp is None:
        fourthWindow.close()

    # If the button "Назад" is pressed
    elif temp == 'Назад':
        fourthWindow.close()
        thirdPage.main()

    # The button "Напред" is pressed
    else:
        fourthWindow.close()
        nextWindow.main()
        


if __name__ == "__main__":
    main()

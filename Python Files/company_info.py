import PySimpleGUI as sg
import company_correspondece_address as next_window
import name_and_translated_name as previous_window

def main():
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
        [sg.Text('Телефон')],
        [sg.Input()],
        [sg.Text('Факс')],
        [sg.Input()],
        [sg.Text('Адрес на електронна поща')],
        [sg.Input()],
        [sg.Text('Интернет страница')],
        [sg.Input()],
        [sg.Button('Назад'), sg.Button('Напред')]
    ]

    window = sg.Window('Информация за компанията', layout,  element_justification="center", font="Helvetica 12", icon="../Logo.ico")
    event, values = window.read()

    if event == 'Назад':
        window.close()
        previous_window.main()

    # If the application is closed by the "X" button
    if event is None:
        window.close()

    # The button "Напред" is pressed
    else:
        window.close()
        next_window.main()


if __name__ == "__main__":
    main()

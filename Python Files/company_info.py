import PySimpleGUI as sg

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
        [sg.Button('Назад'), sg.Button('Напред')]
    ]

    window = sg.Window('Информация за компанията', layout, font="Helvetica 12", icon="../Logo.ico", element_justification="center")
    event, values = window.read()


main()

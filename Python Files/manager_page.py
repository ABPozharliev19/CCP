import PySimpleGUI as sg
import activity_page as previous_page
import capital_owner as next_page


def main():
    layout = [
        [sg.Text('Име')],
        [sg.Input()],
        [sg.Text('ЕГН/ЛНЧ/Дата на раждане')],
        [sg.Input()],
        [sg.Text('Държава')],
        [sg.Input()],
        [sg.Button('Назад'), sg.Button('Напред') ]
    ]

    window = sg.Window('Управител', layout, font="Helvetica 12", icon="../Logo.ico")
    events, values = window.read()

    if events == 'Назад':
        window.close()
        previous_page.main()
    elif events is None:
        window.close()
    else:
        window.close()
        next_page.main()



if __name__ == "__main__":
    main()
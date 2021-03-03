import PySimpleGUI as sg
import company_correspondece_address as previous_page

def main():
    layout = [
        [sg.Text('Въвдете предмета на дейност:',justification='center')],
        [sg.Multiline(pad=(2, 2), size=(45,5))],
        [sg.Button('Назад', size=(10,1),  pad=(2,2)), sg.Button('Напред',size=(10,1),  pad=(2,2))]]

    layout_message = [
        [sg.Text('В следващото поле напишете предмета на дейност на новата ви фирма.')],
        [ sg.Button('Напред')]
    ]

    message_window = sg.Window("Поле за въвеждане",layout_message,  font="Helvetica 12", icon="../Logo.ico")

    window = sg.Window('Предмет на дейност', layout, font="Helvetica 12", icon="../Logo.ico", element_justification="center")

    event, values = message_window.read()

    if event == 'Напред':
        message_window.close()
        event, values = window.read()
        if event is None:
            window.close()
        elif event == 'Напред':
            pass
        else:
            window.close()
            previous_page.main()


if __name__ == "__main__":
    main()
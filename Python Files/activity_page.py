import PySimpleGUI as sg
import manager_page as next_page
import list_of_companies
import subject_activity_page as previous_page


def main():
    layout = [
        [sg.Text('Искате ли да въведете дейност по НКИД?')],
        [sg.Button('Не, не искам.'), sg.Button('Да, искам.')]
    ]

    activity_layout = [
        [sg.Text('Група по НКИД')],
        [sg.Combo(list_of_companies.my_list, size=(44,10))],
        [sg.Text('Клас по НКИД')],
        [sg.Input()],
        [sg.Button('Назад'), sg.Button('Напред')]
    ]

    ask_window = sg.Window('Основна дейност по НКИД', layout, font="Helvetica 12" , element_justification='center', icon="../Logo.ico" )
    event, values = ask_window.read()

    if event == 'Не, не искам.':
        ask_window.close()
        next_page.main()

    elif event == 'Да, искам.':
        ask_window.close()
        activity_window = sg.Window('Основна дейност по НКИД', activity_layout, font="Helvetica 12" , element_justification='center', icon="../Logo.ico")
        event, values = activity_window.read()
        print(values)
        if event == 'Напред':
            activity_window.close()
            next_page.main()
        elif event is None:
            activity_window.close()
        else:
            activity_window.close()
            previous_page.main()


if __name__ == "__main__":
    main()
import PySimpleGUI as sg
import company_info as nextWindow



def main():
    layout = [
        [sg.Text("Фирма / Наименование")],
        [sg.Input()],
        [sg.Text("Изписване на чужд език")],
        [sg.Input()],
        [sg.Button('Напред')]

    ]

    window = sg.Window("Наименование на фирмата", layout, font="Helvetica 12")
    event, values = window.read()

    if event is None:
        window.close()

    elif event == "Напред":
        window.close()
        nextWindow.main()



if __name__ == "__main__":
    main()

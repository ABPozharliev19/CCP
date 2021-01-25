import PySimpleGUI as sg


def main():
    layout = [
        [sg.Text("Фирма / Наименование")],
        [sg.Input()],
        [sg.Text("Изписване на чужд език")],
        [sg.Input()]

    ]

    window = sg.Window("Наименование на фирмата", layout, font="Helvetica 12")
    event, values = window.read()


if __name__ == "__main__":
    main()

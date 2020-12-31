import PySimpleGUI as sg

def main():
    layout = [
        [sg.Text('Държава')],
        [sg.Input()],
        # [sg.]

    ]

    thirdWindow = sg.Window('Постоянен адрес', layout, font = "Helvetica 12")
    thirdWindow.read()


if __name__ == "__main__":
    main()
import PySimpleGUI as sg

def main():
    layout = [
        [sg.Text('Въведетe държавата на раждане')],
        [sg.Input()],
        [sg.Text('Въведете населеното място на раждане')],
        [sg.Input()],
        [sg.Button('Напред')]
    ]
    second_window = sg.Window('Начален прозорец', layout, font="Helvetica 12")
    temp, place_of_birth = second_window.read()
    print(place_of_birth)


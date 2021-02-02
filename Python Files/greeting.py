import PySimpleGUI as sg
import name_and_translated_name as nextWindow

def main():
    layout = [
        [sg.Image('Logo.png')],
        [sg.Text('От тук започва истинското регистриране на фирмата.\n В тази секция ще въведете цялата информация за вашата фирма. \n За да продължите напред, натиснете бутона Напред', justification="center")],
        [sg.Button('Напред', size=(10,1))]
    ]

    window = sg.Window('Кон', layout, element_justification='center')
    event, values = window.read()


    if event == "Напред":
        window.close()
        nextWindow.main()        



if __name__ == "__main__":
    main()
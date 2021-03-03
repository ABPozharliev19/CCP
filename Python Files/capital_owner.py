import PySimpleGUI as sg
import manager_page as previous_page
import backend
"""
Актуален дружествен договор/учредителен акт/устав
Декларация относно истинността на заявените за вписване обстоятелства и приемането на представените за обявяване актове
Декларация по чл. 141, ал. 8 от Търговския закон
Декларация по чл. 142
Договор за управление
Документ за внесен в банка капитал
Документ за внесена държавна такса
Нотариално заверено съгласие и образец от саморъчния подпис на управител
Протокол / Решение на едноличния собственик на капитала
"""


def main():
    layout = [
        [sg.Text('Размер')],
        [sg.Input(), sg.Text('лв')],
        [sg.Button('Назад'), sg.Button('Напред')]
    ]

    window = sg.Window('Капитал', layout,  font="Helvetica 12", icon="../Logo.ico" )
    event, values = window.read()

    if event == 'Назад':
        window.close()
        previous_page.main()
    elif event is None:
        window.close()

    else:
        backend.main()




if __name__ == "__main__":
    main()

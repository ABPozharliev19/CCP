import PySimpleGUI as sg
from logInCheck import *
# from BackEnd import *
from mainFrontEnd import *

sg.popup('Welcome to CCP', custom_text = 'Next')

login_window = [
    [sg.Text('Enter your email or username')],
    [sg.Input()],
    [sg.Text('Enter your password')],
    [sg.Input()],
    [sg.Button('Log In')]

]

logInWindow = sg.Window('Log In', login_window)

username, password = logInWindow.read()

email_login = password[0]
password_login = password[1]

login_check = check(email_login, password_login)

while True:
    login_check = check(email_login, password_login)

    if login_check == "https://portal.registryagency.bg/":
        sg.popup('Successful login!')
        break

    else:
        login_check = check(email_login, password_login)
        sg.popup('Try again!')
        username, password = logInWindow.read()
        email_login = password[0]
        password_login = password[1]


logInWindow.close()
main()


import PySimpleGUI as sg
from logInCheck import *
import nameAndEGN as firstPage
import welcome as startPage


########## Define and design window layout ###########
login_window = [
    [sg.Text('Enter your email or username')],
    [sg.Input()],
    [sg.Text('Enter your password')],
    [sg.Input()],
    [sg.Button('Log In')]
    ]
############# End of design ###############################

# Define the window
logInWindow = sg.Window('Log In', login_window, font="Helvetica 12", icon="../Logo.ico")

# Show the application and read the information in it
username, password = logInWindow.read()

# Store the information into variables
email_login = password[0]
password_login = password[1]

# Check if the login information is correct
login_check = check(email_login, password_login)

while True:
    login_check = check(email_login, password_login)

    # If the information is true
    if login_check == "https://portal.registryagency.bg/":
        sg.popup('Successful login!')

        break

    # if the information is not true
    else:
        login_check = check(email_login, password_login)
        sg.popup('Try again!')
        username, password = logInWindow.read()
        email_login = password[0]
        password_login = password[1]

logInWindow.close()

firstPage.main()



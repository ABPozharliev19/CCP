import PySimpleGUI as sg
from login_check import *
import name_and_eng as firstPage
import file_operations as file
import list_of_passwords
import login_check_second


########## Define and design window layout ###########
login_window = [
    [sg.Text('Enter your email or username')],
    [sg.Input(key="email")],
    [sg.Text('Enter your password')],
    [sg.Input(password_char="●", key="password")],
    [sg.Button("Import"), sg.Button('Log In')]
    ]
############# End of design ###############################

# Define the window
logInWindow = sg.Window('Log In', login_window, font="Helvetica 12", icon="../Logo.ico")

# Show the application and read the information in it
events, password = logInWindow.read()

print(events)

while True:
    if events == "Import":
        email_updated, password_updated = list_of_passwords.main()
        logInWindow.FindElement("email").update(email_updated)
        logInWindow.FindElement("password").update(password_updated)
        events, password = logInWindow.read()
        email_login = password['email']
        password_login = password['password']
        login_check = check(email_login, password_login)
        if events == "Log In":
            while True:
                login_check =check(email_login, password_login)

                # If the information is true
                if login_check == "https://portal.registryagency.bg/":
                    sg.popup('Successful login!')
                    file.save_to_file(email_login, password_login)
                    break

                # if the information is not true
                else:
                    login_check = check(email_login, password_login)
                    sg.popup('Try again!')
                    username, password = logInWindow.read()
                    email_login = password["email"]
                    password_login = password["password"]

            logInWindow.close()

            firstPage.main()
            break

    # Store the information into variables
    elif events is None:
        logInWindow.close()
        break

    elif events == "Log In":
        print(password)

        email_login = password['email']
        password_login = password['password']

        # Check if the login information is correct
        login_check = login_check_second.check(email_login, password_login)

        while True:
            login_check = login_check_second.check(email_login, password_login)

            # If the information is true
            if login_check == "https://portal.registryagency.bg/":
                sg.popup('Successful login!')
                file.save_to_file(email_login, password_login)

                break

            # if the information is not true
            else:
                login_check_second.check(email_login, password_login)
                sg.popup('Try again!')
                username, password = logInWindow.read()
                email_login = password["email"]
                password_login = password["password"]

        logInWindow.close()

        firstPage.main()
        break




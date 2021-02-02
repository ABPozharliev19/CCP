from selenium import webdriver
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_argument('headless')


try:
    driver = webdriver.Chrome("../chromedriver.exe", options=option)

except Exception:
    driver = webdriver.Chrome("../chromedriver1.exe", options=option)

except:
    driver = webdriver.Chrome("../chromedriver2.exe", options=option)


def check(email, password):
    driver.get(
        "https://login.registryagency.bg/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_mode"
        "%3Dform_post%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fportal.registryagency.bg%252Flogin"
        "%26client_id%3Depzeu.ui.client%26nonce%3Db8e326aa4724a3019dedce167e854726%26state"
        "%3D671b6e62ceb9f322da7d3fc31ccf58e4%26scope%3Dopenid%2520profile%2520epzeu.api%2520offline_access")

    emailLog = driver.find_element_by_id("Username")
    passwordLog = driver.find_element_by_id("Password")

    emailLog.send_keys(email)
    passwordLog.send_keys(password)
    passwordLog.send_keys(Keys.ENTER)

    return driver.current_url





# All the imports we need
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import tokens

driver = webdriver.Chrome(tokens.PATH)  # Setting up the webdriver

# Getting the login info
emailForLogIn = tokens.email
passwordForLogIn = tokens.password

# Test variables for debugging
Name = "Георги Стоянов Димитров"
EGN = "0348011188"

placeOfBirth = "България"
cityOfBirth = "Бургас"

postCode = "8000"
country_live = "България"
city_live = "Бургас"
region_live = "Бургас"
neighborhood_live = "Славейков"
street_live = "Гладстон"

companyName = "Кон"
translatedCompanyName = "Kon"
sAddress = "Бургас"
seatAddressPostCode = "8000"
seatAddressHousingEstate = "Въздраждане"
seatAddressStreat = "Гладстон"


def logIn(email, password):  # First function to Log in
    driver.get(
        "https://login.registryagency.bg/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fresponse_mode"
        "%3Dform_post%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fportal.registryagency.bg%252Flogin"
        "%26client_id%3Depzeu.ui.client%26nonce%3Db8e326aa4724a3019dedce167e854726%26state"
        "%3D671b6e62ceb9f322da7d3fc31ccf58e4%26scope%3Dopenid%2520profile%2520epzeu.api%2520offline_access")

    emailLog = driver.find_element_by_id("Username") # Search for the Username input
    passwordLog = driver.find_element_by_id("Password") # Search for the Password input

    # Send the login information
    emailLog.send_keys(email)
    passwordLog.send_keys(password)
    # Press enter for the login to be done
    passwordLog.send_keys(Keys.ENTER)

    # Function to fill all the information in the first page


def registerCompanyPage1(Name, EGN, birthPlace, cityOfBirth, countryOfLife, cityOfLife, regionOfLife, nbHoodOfLife,streetOfLife, postCode):

    driver.get("https://portal.registryagency.bg/CR/applications/ApplicationProcesses/A4")  # Go to the web page
    time.sleep(5)  # Wait for the page to load

    cookieButton = driver.find_element_by_xpath("/html/body/aside/div/div/div[2]/button")
    cookieButton.click()

    driver.maximize_window()

    driver.execute_script("window.scrollTo(0, 500)")

    # Search for the
    nameForm = driver.find_element_by_id("application_applicants.applicantsList.[0].person.name")
    nameForm.send_keys(Name)

    EGNForm = driver.find_element_by_id("application_applicants.applicantsList.[0].person.indent")
    EGNForm.send_keys(EGN)

    birthPlaceForm = driver.find_element_by_id("application_applicants.applicantsList.[0].birthPlace.country")
    birthPlaceForm.send_keys(birthPlace)

    cityOfBirthForm = driver.find_element_by_id("application_applicants.applicantsList.[0].birthPlace.place")
    cityOfBirthForm.send_keys(cityOfBirth)

    countryOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.country")
    countryOfLifeForm.click()
    countryOfLifeForm.clear()
    countryOfLifeForm.send_keys(countryOfLife)

    Form = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[4]/div[2]/div/span/ul/li")))
    Form.click()

    cityOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.settlement")
    cityOfLifeForm.click()
    cityOfLifeForm.send_keys(cityOfLife)

    FormTemp = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[4]/div[3]/div[1]/span/ul/li")))
    FormTemp.click()

    postCodeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.postCode")
    postCodeForm.send_keys(postCode)

    nbHoodOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.housingEstate")
    nbHoodOfLifeForm.send_keys(nbHoodOfLife)

    streetOfLifeForm = driver.find_element_by_id("application_applicants.applicantsList.[0].address.street")
    streetOfLifeForm.send_keys(streetOfLife)

    driver.execute_script("window.scrollTo(0, 1000)")

    inputButton = driver.find_element_by_xpath("//html/body/div[1]/div[2]/div[2]/div[3]/div/div[3]/div[2]/div/div[1]/label")
    inputButton.click()

    time.sleep(100)


def registerCompanyPage2(companyName, translatedName, sAddress, sAPostCode, sAddressHE, sAddressStreat):
    nameOfCompanyForm = driver.find_element_by_id("application_fields.company.text")
    nameOfCompanyForm.send_keys(companyName)

    translatedCompanyNameForm = driver.find_element_by_id("application_fields.transliteration.text")
    translatedCompanyNameForm.send_keys(translatedName)

    seatAddress = driver.find_element_by_id("application_fields.seat.address.settlement")
    seatAddress.send_keys(sAddress)

    time.sleep(5)

    # TODO Automate it like Page 1

    ''' try:
       Form = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=dab15b44-7611-4fe3-9bfc-0f133af26ff6]/div[1]/div[2]/div[1]/div"))) '''

    seatPostCodeForm = driver.find_element_by_id("application_fields.seat.address.postCode")
    seatPostCodeForm.send_keys(sAPostCode)

    seatAddressHousingEstateForm = driver.find_element_by_id("application_fields.seat.address.housingEstate")
    seatAddressHousingEstateForm.send_keys(sAddressHE)

    seatAddressStreatForm = driver.find_element_by_id("application_fields.seat.address.street")
    seatAddressStreatForm.send_keys(seatAddressStreat)

# TODO Do the rest of the Automation
logIn(emailForLogIn, passwordForLogIn)

registerCompanyPage1(Name, EGN, placeOfBirth, cityOfBirth, country_live, city_live, region_live, neighborhood_live, street_live, postCode)

buttonForNextPageForm = driver.find_element_by_xpath("//button[text()='Продължи']").click()

time.sleep(5)

registerCompanyPage2(companyName, translatedCompanyName, sAddress, seatAddressPostCode, seatAddressHousingEstate,seatAddressStreat)
